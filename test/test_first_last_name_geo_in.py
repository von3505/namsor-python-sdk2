# coding: utf-8

"""
    NamSor API v2

    NamSor API v2 : enpoints to process personal names (gender, cultural origin or ethnicity) in all alphabets or languages. Use GET methods for small tests, but prefer POST methods for higher throughput (batch processing of up to 100 names at a time). Need something you can't find here? We have many more features coming soon. Let us know, we'll do our best to add it!   # noqa: E501

    OpenAPI spec version: 2.0.6
    Contact: contact@namsor.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.models.first_last_name_geo_in import FirstLastNameGeoIn  # noqa: E501
from openapi_client.rest import ApiException


class TestFirstLastNameGeoIn(unittest.TestCase):
    """FirstLastNameGeoIn unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testFirstLastNameGeoIn(self):
        """Test FirstLastNameGeoIn"""
        # FIXME: construct object with mandatory attributes with example values
        # model = openapi_client.models.first_last_name_geo_in.FirstLastNameGeoIn()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
