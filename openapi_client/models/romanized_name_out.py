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


class RomanizedNameOut(object):
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
        'latin_name': 'str',
        'original_name': 'str',
        'source_language': 'str',
        'target_language': 'str',
        'source_script': 'str',
        'target_script': 'str',
        'score': 'float'
    }

    attribute_map = {
        'id': 'id',
        'latin_name': 'latinName',
        'original_name': 'originalName',
        'source_language': 'sourceLanguage',
        'target_language': 'targetLanguage',
        'source_script': 'sourceScript',
        'target_script': 'targetScript',
        'score': 'score'
    }

    def __init__(self, id=None, latin_name=None, original_name=None, source_language=None, target_language=None, source_script=None, target_script=None, score=None):  # noqa: E501
        """RomanizedNameOut - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._latin_name = None
        self._original_name = None
        self._source_language = None
        self._target_language = None
        self._source_script = None
        self._target_script = None
        self._score = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if latin_name is not None:
            self.latin_name = latin_name
        if original_name is not None:
            self.original_name = original_name
        if source_language is not None:
            self.source_language = source_language
        if target_language is not None:
            self.target_language = target_language
        if source_script is not None:
            self.source_script = source_script
        if target_script is not None:
            self.target_script = target_script
        if score is not None:
            self.score = score

    @property
    def id(self):
        """Gets the id of this RomanizedNameOut.  # noqa: E501


        :return: The id of this RomanizedNameOut.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RomanizedNameOut.


        :param id: The id of this RomanizedNameOut.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def latin_name(self):
        """Gets the latin_name of this RomanizedNameOut.  # noqa: E501


        :return: The latin_name of this RomanizedNameOut.  # noqa: E501
        :rtype: str
        """
        return self._latin_name

    @latin_name.setter
    def latin_name(self, latin_name):
        """Sets the latin_name of this RomanizedNameOut.


        :param latin_name: The latin_name of this RomanizedNameOut.  # noqa: E501
        :type: str
        """

        self._latin_name = latin_name

    @property
    def original_name(self):
        """Gets the original_name of this RomanizedNameOut.  # noqa: E501


        :return: The original_name of this RomanizedNameOut.  # noqa: E501
        :rtype: str
        """
        return self._original_name

    @original_name.setter
    def original_name(self, original_name):
        """Sets the original_name of this RomanizedNameOut.


        :param original_name: The original_name of this RomanizedNameOut.  # noqa: E501
        :type: str
        """

        self._original_name = original_name

    @property
    def source_language(self):
        """Gets the source_language of this RomanizedNameOut.  # noqa: E501


        :return: The source_language of this RomanizedNameOut.  # noqa: E501
        :rtype: str
        """
        return self._source_language

    @source_language.setter
    def source_language(self, source_language):
        """Sets the source_language of this RomanizedNameOut.


        :param source_language: The source_language of this RomanizedNameOut.  # noqa: E501
        :type: str
        """

        self._source_language = source_language

    @property
    def target_language(self):
        """Gets the target_language of this RomanizedNameOut.  # noqa: E501


        :return: The target_language of this RomanizedNameOut.  # noqa: E501
        :rtype: str
        """
        return self._target_language

    @target_language.setter
    def target_language(self, target_language):
        """Sets the target_language of this RomanizedNameOut.


        :param target_language: The target_language of this RomanizedNameOut.  # noqa: E501
        :type: str
        """

        self._target_language = target_language

    @property
    def source_script(self):
        """Gets the source_script of this RomanizedNameOut.  # noqa: E501


        :return: The source_script of this RomanizedNameOut.  # noqa: E501
        :rtype: str
        """
        return self._source_script

    @source_script.setter
    def source_script(self, source_script):
        """Sets the source_script of this RomanizedNameOut.


        :param source_script: The source_script of this RomanizedNameOut.  # noqa: E501
        :type: str
        """

        self._source_script = source_script

    @property
    def target_script(self):
        """Gets the target_script of this RomanizedNameOut.  # noqa: E501


        :return: The target_script of this RomanizedNameOut.  # noqa: E501
        :rtype: str
        """
        return self._target_script

    @target_script.setter
    def target_script(self, target_script):
        """Sets the target_script of this RomanizedNameOut.


        :param target_script: The target_script of this RomanizedNameOut.  # noqa: E501
        :type: str
        """

        self._target_script = target_script

    @property
    def score(self):
        """Gets the score of this RomanizedNameOut.  # noqa: E501


        :return: The score of this RomanizedNameOut.  # noqa: E501
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this RomanizedNameOut.


        :param score: The score of this RomanizedNameOut.  # noqa: E501
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
        if not isinstance(other, RomanizedNameOut):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
