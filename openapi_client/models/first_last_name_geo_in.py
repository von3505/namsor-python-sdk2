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


class FirstLastNameGeoIn(object):
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
        'id': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'country_iso2': 'str'
    }

    attribute_map = {
        'id': 'id',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'country_iso2': 'countryIso2'
    }

    def __init__(self, id=None, first_name=None, last_name=None, country_iso2=None):  # noqa: E501
        """FirstLastNameGeoIn - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._first_name = None
        self._last_name = None
        self._country_iso2 = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if country_iso2 is not None:
            self.country_iso2 = country_iso2

    @property
    def id(self):
        """Gets the id of this FirstLastNameGeoIn.  # noqa: E501


        :return: The id of this FirstLastNameGeoIn.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FirstLastNameGeoIn.


        :param id: The id of this FirstLastNameGeoIn.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def first_name(self):
        """Gets the first_name of this FirstLastNameGeoIn.  # noqa: E501


        :return: The first_name of this FirstLastNameGeoIn.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this FirstLastNameGeoIn.


        :param first_name: The first_name of this FirstLastNameGeoIn.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this FirstLastNameGeoIn.  # noqa: E501


        :return: The last_name of this FirstLastNameGeoIn.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this FirstLastNameGeoIn.


        :param last_name: The last_name of this FirstLastNameGeoIn.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def country_iso2(self):
        """Gets the country_iso2 of this FirstLastNameGeoIn.  # noqa: E501


        :return: The country_iso2 of this FirstLastNameGeoIn.  # noqa: E501
        :rtype: str
        """
        return self._country_iso2

    @country_iso2.setter
    def country_iso2(self, country_iso2):
        """Sets the country_iso2 of this FirstLastNameGeoIn.


        :param country_iso2: The country_iso2 of this FirstLastNameGeoIn.  # noqa: E501
        :type: str
        """

        self._country_iso2 = country_iso2

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
        if not isinstance(other, FirstLastNameGeoIn):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
