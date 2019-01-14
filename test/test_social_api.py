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
from com.namsor.sdk2.api.social_api import SocialApi  # noqa: E501
from openapi_client.rest import ApiException


class TestSocialApi(unittest.TestCase):
    """SocialApi unit test stubs"""

    def setUp(self):
        self.api = com.namsor.sdk2.api.social_api.SocialApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_phone_prefix(self):
        """Test case for phone_prefix

        [USES 11 UNITS] Infer the likely country and phone prefix, given a personal name and formatted / unformatted phone number.  # noqa: E501
        """
        pass

    def test_phone_prefix_batch(self):
        """Test case for phone_prefix_batch

        [USES 11 UNITS] Infer the likely country and phone prefix, of up to 1000 personal names, detecting automatically the local context given a name and formatted / unformatted phone number.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
