# coding: utf-8

"""
    NamSor API v2

    NamSor API v2 : enpoints to process personal names (gender, cultural origin or ethnicity) in all alphabets or languages. Use GET methods for small tests, but prefer POST methods for higher throughput (batch processing of up to 100 names at a time). Need something you can't find here? We have many more features coming soon. Let us know, we'll do our best to add it!   # noqa: E501

    OpenAPI spec version: 2.0.6
    Contact: contact@namsor.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class APIPlansOut(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'usage_ratio_for_dupplicates': 'int',
        'currency_iso3': 'str',
        'currency_symbol': 'str',
        'plans': 'list[APIPlanOut]'
    }

    attribute_map = {
        'usage_ratio_for_dupplicates': 'usageRatioForDupplicates',
        'currency_iso3': 'currencyIso3',
        'currency_symbol': 'currencySymbol',
        'plans': 'plans'
    }

    def __init__(self, usage_ratio_for_dupplicates=None, currency_iso3=None, currency_symbol=None, plans=None):  # noqa: E501
        """APIPlansOut - a model defined in OpenAPI"""  # noqa: E501

        self._usage_ratio_for_dupplicates = None
        self._currency_iso3 = None
        self._currency_symbol = None
        self._plans = None
        self.discriminator = None

        if usage_ratio_for_dupplicates is not None:
            self.usage_ratio_for_dupplicates = usage_ratio_for_dupplicates
        if currency_iso3 is not None:
            self.currency_iso3 = currency_iso3
        if currency_symbol is not None:
            self.currency_symbol = currency_symbol
        if plans is not None:
            self.plans = plans

    @property
    def usage_ratio_for_dupplicates(self):
        """Gets the usage_ratio_for_dupplicates of this APIPlansOut.  # noqa: E501


        :return: The usage_ratio_for_dupplicates of this APIPlansOut.  # noqa: E501
        :rtype: int
        """
        return self._usage_ratio_for_dupplicates

    @usage_ratio_for_dupplicates.setter
    def usage_ratio_for_dupplicates(self, usage_ratio_for_dupplicates):
        """Sets the usage_ratio_for_dupplicates of this APIPlansOut.


        :param usage_ratio_for_dupplicates: The usage_ratio_for_dupplicates of this APIPlansOut.  # noqa: E501
        :type: int
        """

        self._usage_ratio_for_dupplicates = usage_ratio_for_dupplicates

    @property
    def currency_iso3(self):
        """Gets the currency_iso3 of this APIPlansOut.  # noqa: E501


        :return: The currency_iso3 of this APIPlansOut.  # noqa: E501
        :rtype: str
        """
        return self._currency_iso3

    @currency_iso3.setter
    def currency_iso3(self, currency_iso3):
        """Sets the currency_iso3 of this APIPlansOut.


        :param currency_iso3: The currency_iso3 of this APIPlansOut.  # noqa: E501
        :type: str
        """

        self._currency_iso3 = currency_iso3

    @property
    def currency_symbol(self):
        """Gets the currency_symbol of this APIPlansOut.  # noqa: E501


        :return: The currency_symbol of this APIPlansOut.  # noqa: E501
        :rtype: str
        """
        return self._currency_symbol

    @currency_symbol.setter
    def currency_symbol(self, currency_symbol):
        """Sets the currency_symbol of this APIPlansOut.


        :param currency_symbol: The currency_symbol of this APIPlansOut.  # noqa: E501
        :type: str
        """

        self._currency_symbol = currency_symbol

    @property
    def plans(self):
        """Gets the plans of this APIPlansOut.  # noqa: E501


        :return: The plans of this APIPlansOut.  # noqa: E501
        :rtype: list[APIPlanOut]
        """
        return self._plans

    @plans.setter
    def plans(self, plans):
        """Sets the plans of this APIPlansOut.


        :param plans: The plans of this APIPlansOut.  # noqa: E501
        :type: list[APIPlanOut]
        """

        self._plans = plans

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, APIPlansOut):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
