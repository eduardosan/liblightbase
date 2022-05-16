FROM python:3.7.13

WORKDIR /usr/src/app
ENV PYTHONUNBUFFERED 0
ENV PYTHONIOENCODING  utf-8

# Set Timezone
ENV TZ=America/Sao_Paulo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN echo "America/Sao_Paulo" > /etc/timezone; dpkg-reconfigure -f noninteractive tzdata

# Configure locale
RUN apt-get update && apt-get install -y locales && rm -rf /var/lib/apt/lists/*
RUN echo "pt_BR.UTF-8 UTF-8" >> /etc/locale.gen
RUN locale-gen
RUN export LANGUAGE="pt_BR.UTF-8"; export LANG="pt_BR.UTF-8"; export LC_ALL="pt_BR.UTF-8"; locale-gen "pt_BR.UTF-8"; DEBIAN_FRONTEND=noninteractive dpkg-reconfigure locales

# Necessário limpar esses arquivos para rodar os testes dentro do Docker
COPY . .
RUN find . -name '*.py[odc]' -type f -delete
RUN find . -name '__pycache__' -type d -delete
RUN rm -rf *.egg-info .cache .eggs build dist dists


# Instala testes para rodar dentro do container
RUN pip install --no-cache-dir -e ".[testing]"

CMD [ "python", "./setup.py" , "develop" ]