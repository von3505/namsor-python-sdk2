# coding: utf-8

"""
    NamSor API v2

    NamSor API v2 : enpoints to process personal names (gender, cultural origin or ethnicity) in all alphabets or languages. Use GET methods for small tests, but prefer POST methods for higher throughput (batch processing of up to 100 names at a time). Need something you can't find here? We have many more features coming soon. Let us know, we'll do our best to add it!   # noqa: E501

    OpenAPI spec version: 2.0.7
    Contact: contact@namsor.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.models.nam_sor_counter_out import NamSorCounterOut  # noqa: E501
from openapi_client.rest import ApiException


class TestNamSorCounterOut(unittest.TestCase):
    """NamSorCounterOut unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNamSorCounterOut(self):
        """Test NamSorCounterOut"""
        # FIXME: construct object with mandatory attributes with example values
        # model = openapi_client.models.nam_sor_counter_out.NamSorCounterOut()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
