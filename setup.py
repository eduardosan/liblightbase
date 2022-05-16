from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()
with open(os.path.join(here, 'VERSION')) as f:
    VERSION = f.read()

requires = [
    'voluptuous == 0.8.7',
    'ply == 3.4',
    'decorator == 3.4.0',
    'requests == 2.3.0',
    'python-dateutil == 2.2',
    'six == 1.7.2',
    'jsonpath-rw == 1.3.0'
]

tests_require = [
    'httpretty',  # py3 compat
    'pytest',  # includes virtualenv
    'pytest-cov',
    'gitchangelog',
]

setup(name='liblightbase',
      version=VERSION,
      description="LightBase Library",
      long_description="""\
      LightBase Library""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='lightbase-neo ligthbase json database library',
      author='Lightbase',
      author_email='info@lightbase.com.br',
      url='http://lightbase.com.br/',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=requires,
      extras_require={
          'testing': tests_require,
      },
  )
