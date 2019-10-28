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


class SourceDetailedMetricsOut(object):
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
        'source': 'APIKeyOut',
        'ai_estimate_total': 'int',
        'ai_estimate_precision': 'float',
        'ai_estimate_recall': 'float',
        'metric_time_stamp': 'int',
        'ai_start_time': 'int',
        'ai_learn_total': 'int',
        'snapshot_date': 'int',
        'expected_class_metrics': 'list[ExpectedClassMetricsOut]'
    }

    attribute_map = {
        'classifier_name': 'classifierName',
        'source': 'source',
        'ai_estimate_total': 'aiEstimateTotal',
        'ai_estimate_precision': 'aiEstimatePrecision',
        'ai_estimate_recall': 'aiEstimateRecall',
        'metric_time_stamp': 'metricTimeStamp',
        'ai_start_time': 'aiStartTime',
        'ai_learn_total': 'aiLearnTotal',
        'snapshot_date': 'snapshotDate',
        'expected_class_metrics': 'expectedClassMetrics'
    }

    def __init__(self, classifier_name=None, source=None, ai_estimate_total=None, ai_estimate_precision=None, ai_estimate_recall=None, metric_time_stamp=None, ai_start_time=None, ai_learn_total=None, snapshot_date=None, expected_class_metrics=None):  # noqa: E501
        """SourceDetailedMetricsOut - a model defined in OpenAPI"""  # noqa: E501

        self._classifier_name = None
        self._source = None
        self._ai_estimate_total = None
        self._ai_estimate_precision = None
        self._ai_estimate_recall = None
        self._metric_time_stamp = None
        self._ai_start_time = None
        self._ai_learn_total = None
        self._snapshot_date = None
        self._expected_class_metrics = None
        self.discriminator = None

        if classifier_name is not None:
            self.classifier_name = classifier_name
        if source is not None:
            self.source = source
        if ai_estimate_total is not None:
            self.ai_estimate_total = ai_estimate_total
        if ai_estimate_precision is not None:
            self.ai_estimate_precision = ai_estimate_precision
        if ai_estimate_recall is not None:
            self.ai_estimate_recall = ai_estimate_recall
        if metric_time_stamp is not None:
            self.metric_time_stamp = metric_time_stamp
        if ai_start_time is not None:
            self.ai_start_time = ai_start_time
        if ai_learn_total is not None:
            self.ai_learn_total = ai_learn_total
        if snapshot_date is not None:
            self.snapshot_date = snapshot_date
        if expected_class_metrics is not None:
            self.expected_class_metrics = expected_class_metrics

    @property
    def classifier_name(self):
        """Gets the classifier_name of this SourceDetailedMetricsOut.  # noqa: E501


        :return: The classifier_name of this SourceDetailedMetricsOut.  # noqa: E501
        :rtype: str
        """
        return self._classifier_name

    @classifier_name.setter
    def classifier_name(self, classifier_name):
        """Sets the classifier_name of this SourceDetailedMetricsOut.


        :param classifier_name: The classifier_name of this SourceDetailedMetricsOut.  # noqa: E501
        :type: str
        """

        self._classifier_name = classifier_name

    @property
    def source(self):
        """Gets the source of this SourceDetailedMetricsOut.  # noqa: E501


        :return: The source of this SourceDetailedMetricsOut.  # noqa: E501
        :rtype: APIKeyOut
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this SourceDetailedMetricsOut.


        :param source: The source of this SourceDetailedMetricsOut.  # noqa: E501
        :type: APIKeyOut
        """

        self._source = source

    @property
    def ai_estimate_total(self):
        """Gets the ai_estimate_total of this SourceDetailedMetricsOut.  # noqa: E501


        :return: The ai_estimate_total of this SourceDetailedMetricsOut.  # noqa: E501
        :rtype: int
        """
        return self._ai_estimate_total

    @ai_estimate_total.setter
    def ai_estimate_total(self, ai_estimate_total):
        """Sets the ai_estimate_total of this SourceDetailedMetricsOut.


        :param ai_estimate_total: The ai_estimate_total of this SourceDetailedMetricsOut.  # noqa: E501
        :type: int
        """

        self._ai_estimate_total = ai_estimate_total

    @property
    def ai_estimate_precision(self):
        """Gets the ai_estimate_precision of this SourceDetailedMetricsOut.  # noqa: E501


        :return: The ai_estimate_precision of this SourceDetailedMetricsOut.  # noqa: E501
        :rtype: float
        """
        return self._ai_estimate_precision

    @ai_estimate_precision.setter
    def ai_estimate_precision(self, ai_estimate_precision):
        """Sets the ai_estimate_precision of this SourceDetailedMetricsOut.


        :param ai_estimate_precision: The ai_estimate_precision of this SourceDetailedMetricsOut.  # noqa: E501
        :type: float
        """

        self._ai_estimate_precision = ai_estimate_precision

    @property
    def ai_estimate_recall(self):
        """Gets the ai_estimate_recall of this SourceDetailedMetricsOut.  # noqa: E501


        :return: The ai_estimate_recall of this SourceDetailedMetricsOut.  # noqa: E501
        :rtype: float
        """
        return self._ai_estimate_recall

    @ai_estimate_recall.setter
    def ai_estimate_recall(self, ai_estimate_recall):
        """Sets the ai_estimate_recall of this SourceDetailedMetricsOut.


        :param ai_estimate_recall: The ai_estimate_recall of this SourceDetailedMetricsOut.  # noqa: E501
        :type: float
        """

        self._ai_estimate_recall = ai_estimate_recall

    @property
    def metric_time_stamp(self):
        """Gets the metric_time_stamp of this SourceDetailedMetricsOut.  # noqa: E501


        :return: The metric_time_stamp of this SourceDetailedMetricsOut.  # noqa: E501
        :rtype: int
        """
        return self._metric_time_stamp

    @metric_time_stamp.setter
    def metric_time_stamp(self, metric_time_stamp):
        """Sets the metric_time_stamp of this SourceDetailedMetricsOut.


        :param metric_time_stamp: The metric_time_stamp of this SourceDetailedMetricsOut.  # noqa: E501
        :type: int
        """

        self._metric_time_stamp = metric_time_stamp

    @property
    def ai_start_time(self):
        """Gets the ai_start_time of this SourceDetailedMetricsOut.  # noqa: E501


        :return: The ai_start_time of this SourceDetailedMetricsOut.  # noqa: E501
        :rtype: int
        """
        return self._ai_start_time

    @ai_start_time.setter
    def ai_start_time(self, ai_start_time):
        """Sets the ai_start_time of this SourceDetailedMetricsOut.


        :param ai_start_time: The ai_start_time of this SourceDetailedMetricsOut.  # noqa: E501
        :type: int
        """

        self._ai_start_time = ai_start_time

    @property
    def ai_learn_total(self):
        """Gets the ai_learn_total of this SourceDetailedMetricsOut.  # noqa: E501


        :return: The ai_learn_total of this SourceDetailedMetricsOut.  # noqa: E501
        :rtype: int
        """
        return self._ai_learn_total

    @ai_learn_total.setter
    def ai_learn_total(self, ai_learn_total):
        """Sets the ai_learn_total of this SourceDetailedMetricsOut.


        :param ai_learn_total: The ai_learn_total of this SourceDetailedMetricsOut.  # noqa: E501
        :type: int
        """

        self._ai_learn_total = ai_learn_total

    @property
    def snapshot_date(self):
        """Gets the snapshot_date of this SourceDetailedMetricsOut.  # noqa: E501


        :return: The snapshot_date of this SourceDetailedMetricsOut.  # noqa: E501
        :rtype: int
        """
        return self._snapshot_date

    @snapshot_date.setter
    def snapshot_date(self, snapshot_date):
        """Sets the snapshot_date of this SourceDetailedMetricsOut.


        :param snapshot_date: The snapshot_date of this SourceDetailedMetricsOut.  # noqa: E501
        :type: int
        """

        self._snapshot_date = snapshot_date

    @property
    def expected_class_metrics(self):
        """Gets the expected_class_metrics of this SourceDetailedMetricsOut.  # noqa: E501


        :return: The expected_class_metrics of this SourceDetailedMetricsOut.  # noqa: E501
        :rtype: list[ExpectedClassMetricsOut]
        """
        return self._expected_class_metrics

    @expected_class_metrics.setter
    def expected_class_metrics(self, expected_class_metrics):
        """Sets the expected_class_metrics of this SourceDetailedMetricsOut.


        :param expected_class_metrics: The expected_class_metrics of this SourceDetailedMetricsOut.  # noqa: E501
        :type: list[ExpectedClassMetricsOut]
        """

        self._expected_class_metrics = expected_class_metrics

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
        if not isinstance(other, SourceDetailedMetricsOut):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
