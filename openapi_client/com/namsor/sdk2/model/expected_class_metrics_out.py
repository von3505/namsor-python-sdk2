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


class ExpectedClassMetricsOut(object):
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
        'classifier_name': 'str',
        'expected_class': 'str',
        'ai_estimate_total': 'int',
        'ai_estimate_precision': 'float',
        'ai_estimate_recall': 'float',
        'ai_learn_total': 'int'
    }

    attribute_map = {
        'classifier_name': 'classifierName',
        'expected_class': 'expectedClass',
        'ai_estimate_total': 'aiEstimateTotal',
        'ai_estimate_precision': 'aiEstimatePrecision',
        'ai_estimate_recall': 'aiEstimateRecall',
        'ai_learn_total': 'aiLearnTotal'
    }

    def __init__(self, classifier_name=None, expected_class=None, ai_estimate_total=None, ai_estimate_precision=None, ai_estimate_recall=None, ai_learn_total=None):  # noqa: E501
        """ExpectedClassMetricsOut - a model defined in OpenAPI"""  # noqa: E501

        self._classifier_name = None
        self._expected_class = None
        self._ai_estimate_total = None
        self._ai_estimate_precision = None
        self._ai_estimate_recall = None
        self._ai_learn_total = None
        self.discriminator = None

        if classifier_name is not None:
            self.classifier_name = classifier_name
        if expected_class is not None:
            self.expected_class = expected_class
        if ai_estimate_total is not None:
            self.ai_estimate_total = ai_estimate_total
        if ai_estimate_precision is not None:
            self.ai_estimate_precision = ai_estimate_precision
        if ai_estimate_recall is not None:
            self.ai_estimate_recall = ai_estimate_recall
        if ai_learn_total is not None:
            self.ai_learn_total = ai_learn_total

    @property
    def classifier_name(self):
        """Gets the classifier_name of this ExpectedClassMetricsOut.  # noqa: E501


        :return: The classifier_name of this ExpectedClassMetricsOut.  # noqa: E501
        :rtype: str
        """
        return self._classifier_name

    @classifier_name.setter
    def classifier_name(self, classifier_name):
        """Sets the classifier_name of this ExpectedClassMetricsOut.


        :param classifier_name: The classifier_name of this ExpectedClassMetricsOut.  # noqa: E501
        :type: str
        """

        self._classifier_name = classifier_name

    @property
    def expected_class(self):
        """Gets the expected_class of this ExpectedClassMetricsOut.  # noqa: E501


        :return: The expected_class of this ExpectedClassMetricsOut.  # noqa: E501
        :rtype: str
        """
        return self._expected_class

    @expected_class.setter
    def expected_class(self, expected_class):
        """Sets the expected_class of this ExpectedClassMetricsOut.


        :param expected_class: The expected_class of this ExpectedClassMetricsOut.  # noqa: E501
        :type: str
        """

        self._expected_class = expected_class

    @property
    def ai_estimate_total(self):
        """Gets the ai_estimate_total of this ExpectedClassMetricsOut.  # noqa: E501


        :return: The ai_estimate_total of this ExpectedClassMetricsOut.  # noqa: E501
        :rtype: int
        """
        return self._ai_estimate_total

    @ai_estimate_total.setter
    def ai_estimate_total(self, ai_estimate_total):
        """Sets the ai_estimate_total of this ExpectedClassMetricsOut.


        :param ai_estimate_total: The ai_estimate_total of this ExpectedClassMetricsOut.  # noqa: E501
        :type: int
        """

        self._ai_estimate_total = ai_estimate_total

    @property
    def ai_estimate_precision(self):
        """Gets the ai_estimate_precision of this ExpectedClassMetricsOut.  # noqa: E501


        :return: The ai_estimate_precision of this ExpectedClassMetricsOut.  # noqa: E501
        :rtype: float
        """
        return self._ai_estimate_precision

    @ai_estimate_precision.setter
    def ai_estimate_precision(self, ai_estimate_precision):
        """Sets the ai_estimate_precision of this ExpectedClassMetricsOut.


        :param ai_estimate_precision: The ai_estimate_precision of this ExpectedClassMetricsOut.  # noqa: E501
        :type: float
        """

        self._ai_estimate_precision = ai_estimate_precision

    @property
    def ai_estimate_recall(self):
        """Gets the ai_estimate_recall of this ExpectedClassMetricsOut.  # noqa: E501


        :return: The ai_estimate_recall of this ExpectedClassMetricsOut.  # noqa: E501
        :rtype: float
        """
        return self._ai_estimate_recall

    @ai_estimate_recall.setter
    def ai_estimate_recall(self, ai_estimate_recall):
        """Sets the ai_estimate_recall of this ExpectedClassMetricsOut.


        :param ai_estimate_recall: The ai_estimate_recall of this ExpectedClassMetricsOut.  # noqa: E501
        :type: float
        """

        self._ai_estimate_recall = ai_estimate_recall

    @property
    def ai_learn_total(self):
        """Gets the ai_learn_total of this ExpectedClassMetricsOut.  # noqa: E501


        :return: The ai_learn_total of this ExpectedClassMetricsOut.  # noqa: E501
        :rtype: int
        """
        return self._ai_learn_total

    @ai_learn_total.setter
    def ai_learn_total(self, ai_learn_total):
        """Sets the ai_learn_total of this ExpectedClassMetricsOut.


        :param ai_learn_total: The ai_learn_total of this ExpectedClassMetricsOut.  # noqa: E501
        :type: int
        """

        self._ai_learn_total = ai_learn_total

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
        if not isinstance(other, ExpectedClassMetricsOut):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
