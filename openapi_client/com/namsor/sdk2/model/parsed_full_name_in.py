# coding: utf-8

"""
    NamSor API v2

    NamSor API v2 : enpoints to process personal names (gender, cultural origin or ethnicity) in all alphabets or languages. Use GET methods for small tests, but prefer POST methods for higher throughput (batch processing of up to 1000 names at a time). Need something you can't find here? We have many more features coming soon. Let us know, we'll do our best to add it!   # noqa: E501

    OpenAPI spec version: 2.0.2-beta
    Contact: contact@namsor.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class ParsedFullNameIn(object):
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
        'prefix_or_title': 'str',
        'suffix': 'str',
        'middle_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'prefix_or_title': 'prefixOrTitle',
        'suffix': 'suffix',
        'middle_name': 'middleName'
    }

    def __init__(self, id=None, first_name=None, last_name=None, prefix_or_title=None, suffix=None, middle_name=None):  # noqa: E501
        """ParsedFullNameIn - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._first_name = None
        self._last_name = None
        self._prefix_or_title = None
        self._suffix = None
        self._middle_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if prefix_or_title is not None:
            self.prefix_or_title = prefix_or_title
        if suffix is not None:
            self.suffix = suffix
        if middle_name is not None:
            self.middle_name = middle_name

    @property
    def id(self):
        """Gets the id of this ParsedFullNameIn.  # noqa: E501


        :return: The id of this ParsedFullNameIn.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ParsedFullNameIn.


        :param id: The id of this ParsedFullNameIn.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def first_name(self):
        """Gets the first_name of this ParsedFullNameIn.  # noqa: E501


        :return: The first_name of this ParsedFullNameIn.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this ParsedFullNameIn.


        :param first_name: The first_name of this ParsedFullNameIn.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this ParsedFullNameIn.  # noqa: E501


        :return: The last_name of this ParsedFullNameIn.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this ParsedFullNameIn.


        :param last_name: The last_name of this ParsedFullNameIn.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def prefix_or_title(self):
        """Gets the prefix_or_title of this ParsedFullNameIn.  # noqa: E501


        :return: The prefix_or_title of this ParsedFullNameIn.  # noqa: E501
        :rtype: str
        """
        return self._prefix_or_title

    @prefix_or_title.setter
    def prefix_or_title(self, prefix_or_title):
        """Sets the prefix_or_title of this ParsedFullNameIn.


        :param prefix_or_title: The prefix_or_title of this ParsedFullNameIn.  # noqa: E501
        :type: str
        """

        self._prefix_or_title = prefix_or_title

    @property
    def suffix(self):
        """Gets the suffix of this ParsedFullNameIn.  # noqa: E501


        :return: The suffix of this ParsedFullNameIn.  # noqa: E501
        :rtype: str
        """
        return self._suffix

    @suffix.setter
    def suffix(self, suffix):
        """Sets the suffix of this ParsedFullNameIn.


        :param suffix: The suffix of this ParsedFullNameIn.  # noqa: E501
        :type: str
        """

        self._suffix = suffix

    @property
    def middle_name(self):
        """Gets the middle_name of this ParsedFullNameIn.  # noqa: E501


        :return: The middle_name of this ParsedFullNameIn.  # noqa: E501
        :rtype: str
        """
        return self._middle_name

    @middle_name.setter
    def middle_name(self, middle_name):
        """Sets the middle_name of this ParsedFullNameIn.


        :param middle_name: The middle_name of this ParsedFullNameIn.  # noqa: E501
        :type: str
        """

        self._middle_name = middle_name

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
        if not isinstance(other, ParsedFullNameIn):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
