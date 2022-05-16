# -*- coding: utf-8 -*-
import json
import os.path
import httpretty

from liblightbase.lbrest.file import FileREST


@httpretty.activate
def test_file():
    response = {
        'status': 'ok'
    }
    rest_url = 'http://api.brlight.net/api'
    base_test = 'base_tree_lbdoc_test'

    httpretty.register_uri(
        httpretty.POST,
        rest_url + f"/{base_test}/file",
        content_type="application/json",
        body=json.dumps(response),
        status=200
    )

    rest = FileREST(rest_url, base_test)

    here = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(here, './fiénâme.txt')

    with open(filepath, 'r') as f:
        b = f.read()
        n = f.name
        print(n)
    arq = open(filepath, 'r')
    assert arq
    resp = rest.create(arq)
    assert resp



