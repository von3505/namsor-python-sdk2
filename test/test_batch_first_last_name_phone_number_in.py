# coding: utf-8

"""
    NamSor API v2

    NamSor API v2 : enpoints to process personal names (gender, cultural origin or ethnicity) in all alphabets or languages. Use GET methods for small tests, but prefer POST methods for higher throughput (batch processing of up to 1000 names at a time). Need something you can't find here? We have many more features coming soon. Let us know, we'll do our best to add it!   # noqa: E501

    OpenAPI spec version: 2.0.2-beta
    Contact: contact@namsor.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.namsor_sdk2_model.batch_first_last_name_phone_number_in import BatchFirstLastNamePhoneNumberIn  # noqa: E501
from openapi_client.rest import ApiException


class TestBatchFirstLastNamePhoneNumberIn(unittest.TestCase):
    """BatchFirstLastNamePhoneNumberIn unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testBatchFirstLastNamePhoneNumberIn(self):
        """Test BatchFirstLastNamePhoneNumberIn"""
        # FIXME: construct object with mandatory attributes with example values
        # model = openapi_client.models.batch_first_last_name_phone_number_in.BatchFirstLastNamePhoneNumberIn()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()