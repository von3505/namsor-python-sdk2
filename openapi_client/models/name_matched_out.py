# coding: utf-8

"""
    NamSor API v2

    NamSor API v2 : enpoints to process personal names (gender, cultural origin or ethnicity) in all alphabets or languages. Use GET methods for small tests, but prefer POST methods for higher throughput (batch processing of up to 100 names at a time). Need something you can't find here? We have many more features coming soon. Let us know, we'll do our best to add it!   # noqa: E501

    OpenAPI spec version: 2.0.8
    Contact: contact@namsor.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class NameMatchedOut(object):
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
        'match_status': 'str',
        'score': 'float'
    }

    attribute_map = {
        'id': 'id',
        'match_status': 'matchStatus',
        'score': 'score'
    }

    def __init__(self, id=None, match_status=None, score=None):  # noqa: E501
        """NameMatchedOut - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._match_status = None
        self._score = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if match_status is not None:
            self.match_status = match_status
        if score is not None:
            self.score = score

    @property
    def id(self):
        """Gets the id of this NameMatchedOut.  # noqa: E501


        :return: The id of this NameMatchedOut.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NameMatchedOut.


        :param id: The id of this NameMatchedOut.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def match_status(self):
        """Gets the match_status of this NameMatchedOut.  # noqa: E501


        :return: The match_status of this NameMatchedOut.  # noqa: E501
        :rtype: str
        """
        return self._match_status

    @match_status.setter
    def match_status(self, match_status):
        """Sets the match_status of this NameMatchedOut.


        :param match_status: The match_status of this NameMatchedOut.  # noqa: E501
        :type: str
        """

        self._match_status = match_status

    @property
    def score(self):
        """Gets the score of this NameMatchedOut.  # noqa: E501


        :return: The score of this NameMatchedOut.  # noqa: E501
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this NameMatchedOut.


        :param score: The score of this NameMatchedOut.  # noqa: E501
        :type: float
        """

        self._score = score

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
        if not isinstance(other, NameMatchedOut):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
