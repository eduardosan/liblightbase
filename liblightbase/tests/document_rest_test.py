import os.path
import json
import httpretty

from liblightbase.lbutils.conv import document2json
from liblightbase.lbrest.base import BaseREST
from liblightbase.lbrest.document import DocumentREST
from liblightbase.lbsearch.search import Collection
from liblightbase.lbutils.conv import json2base
import unittest


class DocumentRESTTest(unittest.TestCase):
    """
    Test base metaclasses 
    """

    def setUp(self):
        """
        Load data from previous tests and setup test data
        :return:
        """
        # lbjson_test.TestJSON.setUp(self)
        httpretty.enable()
        self.rest_url = 'http://api.brlight.net/api'
        self.base_rest = BaseREST(self.rest_url)
        here = os.path.abspath(os.path.dirname(__file__))

        # Load data
        with open(os.path.join(here, "./fixtures/base.json"), 'r') as fd:
            self.base = json2base(json.load(fd))

        with open(os.path.join(here, "./fixtures/document.json"), 'r') as fd:
            self.document = json.load(fd)

        with open(os.path.join(here, "./fixtures/collection.json"), 'r') as fd:
            self.collection = json.load(fd)

        self.doc_rest = DocumentREST(self.rest_url, self.base)

    def test_get_doc(self):
        httpretty.register_uri(
            httpretty.GET,
            self.rest_url + "/crime/doc/1",
            content_type="application/json",
            body=json.dumps(self.document),
            status=200
        )
        document = self.doc_rest.get(1)
        document_type = self.base.metaclass()
        assert isinstance(document, document_type)

        with open('/tmp/document.json', 'w+') as f:
            f.write(document2json(self.base, document))

    def test_get_doc_colletion(self):
        httpretty.register_uri(
            httpretty.GET,
            self.rest_url + "/crime/doc",
            content_type="application/json",
            body=json.dumps(self.collection),
            status=200
        )

        collection = self.doc_rest.get_collection()
        assert isinstance(collection, Collection)
        assert isinstance(collection.results[0], self.base.metaclass())
