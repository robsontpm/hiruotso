# coding: utf-8
__author__ = 'robson'

from django.test import TestCase
from django.test import Client


class HTTPPagesTest(TestCase):

    def setUp(self):
        pass

    def test_index_page(self):
        # tests if index page can be accessed normally
        client = Client()
        response = client.get('/')
        assert response.status_code == 200

