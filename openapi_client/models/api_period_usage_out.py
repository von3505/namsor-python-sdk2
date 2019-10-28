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


class APIPeriodUsageOut(object):
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
        'subscription': 'APIPlanSubscriptionOut',
        'billing_period': 'APIBillingPeriodUsageOut',
        'overage_excl_tax': 'float',
        'overage_incl_tax': 'float',
        'overage_currency': 'str',
        'overage_quantity': 'int'
    }

    attribute_map = {
        'subscription': 'subscription',
        'billing_period': 'billingPeriod',
        'overage_excl_tax': 'overageExclTax',
        'overage_incl_tax': 'overageInclTax',
        'overage_currency': 'overageCurrency',
        'overage_quantity': 'overageQuantity'
    }

    def __init__(self, subscription=None, billing_period=None, overage_excl_tax=None, overage_incl_tax=None, overage_currency=None, overage_quantity=None):  # noqa: E501
        """APIPeriodUsageOut - a model defined in OpenAPI"""  # noqa: E501

        self._subscription = None
        self._billing_period = None
        self._overage_excl_tax = None
        self._overage_incl_tax = None
        self._overage_currency = None
        self._overage_quantity = None
        self.discriminator = None

        if subscription is not None:
            self.subscription = subscription
        if billing_period is not None:
            self.billing_period = billing_period
        if overage_excl_tax is not None:
            self.overage_excl_tax = overage_excl_tax
        if overage_incl_tax is not None:
            self.overage_incl_tax = overage_incl_tax
        if overage_currency is not None:
            self.overage_currency = overage_currency
        if overage_quantity is not None:
            self.overage_quantity = overage_quantity

    @property
    def subscription(self):
        """Gets the subscription of this APIPeriodUsageOut.  # noqa: E501


        :return: The subscription of this APIPeriodUsageOut.  # noqa: E501
        :rtype: APIPlanSubscriptionOut
        """
        return self._subscription

    @subscription.setter
    def subscription(self, subscription):
        """Sets the subscription of this APIPeriodUsageOut.


        :param subscription: The subscription of this APIPeriodUsageOut.  # noqa: E501
        :type: APIPlanSubscriptionOut
        """

        self._subscription = subscription

    @property
    def billing_period(self):
        """Gets the billing_period of this APIPeriodUsageOut.  # noqa: E501


        :return: The billing_period of this APIPeriodUsageOut.  # noqa: E501
        :rtype: APIBillingPeriodUsageOut
        """
        return self._billing_period

    @billing_period.setter
    def billing_period(self, billing_period):
        """Sets the billing_period of this APIPeriodUsageOut.


        :param billing_period: The billing_period of this APIPeriodUsageOut.  # noqa: E501
        :type: APIBillingPeriodUsageOut
        """

        self._billing_period = billing_period

    @property
    def overage_excl_tax(self):
        """Gets the overage_excl_tax of this APIPeriodUsageOut.  # noqa: E501


        :return: The overage_excl_tax of this APIPeriodUsageOut.  # noqa: E501
        :rtype: float
        """
        return self._overage_excl_tax

    @overage_excl_tax.setter
    def overage_excl_tax(self, overage_excl_tax):
        """Sets the overage_excl_tax of this APIPeriodUsageOut.


        :param overage_excl_tax: The overage_excl_tax of this APIPeriodUsageOut.  # noqa: E501
        :type: float
        """

        self._overage_excl_tax = overage_excl_tax

    @property
    def overage_incl_tax(self):
        """Gets the overage_incl_tax of this APIPeriodUsageOut.  # noqa: E501


        :return: The overage_incl_tax of this APIPeriodUsageOut.  # noqa: E501
        :rtype: float
        """
        return self._overage_incl_tax

    @overage_incl_tax.setter
    def overage_incl_tax(self, overage_incl_tax):
        """Sets the overage_incl_tax of this APIPeriodUsageOut.


        :param overage_incl_tax: The overage_incl_tax of this APIPeriodUsageOut.  # noqa: E501
        :type: float
        """

        self._overage_incl_tax = overage_incl_tax

    @property
    def overage_currency(self):
        """Gets the overage_currency of this APIPeriodUsageOut.  # noqa: E501


        :return: The overage_currency of this APIPeriodUsageOut.  # noqa: E501
        :rtype: str
        """
        return self._overage_currency

    @overage_currency.setter
    def overage_currency(self, overage_currency):
        """Sets the overage_currency of this APIPeriodUsageOut.


        :param overage_currency: The overage_currency of this APIPeriodUsageOut.  # noqa: E501
        :type: str
        """

        self._overage_currency = overage_currency

    @property
    def overage_quantity(self):
        """Gets the overage_quantity of this APIPeriodUsageOut.  # noqa: E501


        :return: The overage_quantity of this APIPeriodUsageOut.  # noqa: E501
        :rtype: int
        """
        return self._overage_quantity

    @overage_quantity.setter
    def overage_quantity(self, overage_quantity):
        """Sets the overage_quantity of this APIPeriodUsageOut.


        :param overage_quantity: The overage_quantity of this APIPeriodUsageOut.  # noqa: E501
        :type: int
        """

        self._overage_quantity = overage_quantity

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
        if not isinstance(other, APIPeriodUsageOut):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
