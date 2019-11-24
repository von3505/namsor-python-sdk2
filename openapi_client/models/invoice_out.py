# coding: utf-8

"""
    NamSor API v2

    NamSor API v2 : enpoints to process personal names (gender, cultural origin or ethnicity) in all alphabets or languages. Use GET methods for small tests, but prefer POST methods for higher throughput (batch processing of up to 100 names at a time). Need something you can't find here? We have many more features coming soon. Let us know, we'll do our best to add it!   # noqa: E501

    OpenAPI spec version: 2.0.7
    Contact: contact@namsor.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class InvoiceOut(object):
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
        'items': 'list[InvoiceItemOut]',
        'user_id': 'str',
        'invoice_id': 'str',
        'is_striped': 'bool',
        'stripe_customer_id': 'str',
        'amount_due': 'int',
        'amount_paid': 'int',
        'amount_remaining': 'int',
        'attempted': 'bool',
        'currency': 'str',
        'invoice_date': 'datetime',
        'due_date': 'datetime',
        'description': 'str',
        'invoice_pdf': 'str',
        'period_start': 'datetime',
        'period_end': 'datetime',
        'receipt_number': 'str',
        'invoice_status': 'str',
        'sub_total': 'int',
        'tax': 'int',
        'tax_percent': 'int',
        'total': 'int'
    }

    attribute_map = {
        'items': 'items',
        'user_id': 'userId',
        'invoice_id': 'invoiceId',
        'is_striped': 'isStriped',
        'stripe_customer_id': 'stripeCustomerId',
        'amount_due': 'amountDue',
        'amount_paid': 'amountPaid',
        'amount_remaining': 'amountRemaining',
        'attempted': 'attempted',
        'currency': 'currency',
        'invoice_date': 'invoiceDate',
        'due_date': 'dueDate',
        'description': 'description',
        'invoice_pdf': 'invoicePdf',
        'period_start': 'periodStart',
        'period_end': 'periodEnd',
        'receipt_number': 'receiptNumber',
        'invoice_status': 'invoiceStatus',
        'sub_total': 'subTotal',
        'tax': 'tax',
        'tax_percent': 'taxPercent',
        'total': 'total'
    }

    def __init__(self, items=None, user_id=None, invoice_id=None, is_striped=None, stripe_customer_id=None, amount_due=None, amount_paid=None, amount_remaining=None, attempted=None, currency=None, invoice_date=None, due_date=None, description=None, invoice_pdf=None, period_start=None, period_end=None, receipt_number=None, invoice_status=None, sub_total=None, tax=None, tax_percent=None, total=None):  # noqa: E501
        """InvoiceOut - a model defined in OpenAPI"""  # noqa: E501

        self._items = None
        self._user_id = None
        self._invoice_id = None
        self._is_striped = None
        self._stripe_customer_id = None
        self._amount_due = None
        self._amount_paid = None
        self._amount_remaining = None
        self._attempted = None
        self._currency = None
        self._invoice_date = None
        self._due_date = None
        self._description = None
        self._invoice_pdf = None
        self._period_start = None
        self._period_end = None
        self._receipt_number = None
        self._invoice_status = None
        self._sub_total = None
        self._tax = None
        self._tax_percent = None
        self._total = None
        self.discriminator = None

        if items is not None:
            self.items = items
        if user_id is not None:
            self.user_id = user_id
        if invoice_id is not None:
            self.invoice_id = invoice_id
        if is_striped is not None:
            self.is_striped = is_striped
        if stripe_customer_id is not None:
            self.stripe_customer_id = stripe_customer_id
        if amount_due is not None:
            self.amount_due = amount_due
        if amount_paid is not None:
            self.amount_paid = amount_paid
        if amount_remaining is not None:
            self.amount_remaining = amount_remaining
        if attempted is not None:
            self.attempted = attempted
        if currency is not None:
            self.currency = currency
        if invoice_date is not None:
            self.invoice_date = invoice_date
        if due_date is not None:
            self.due_date = due_date
        if description is not None:
            self.description = description
        if invoice_pdf is not None:
            self.invoice_pdf = invoice_pdf
        if period_start is not None:
            self.period_start = period_start
        if period_end is not None:
            self.period_end = period_end
        if receipt_number is not None:
            self.receipt_number = receipt_number
        if invoice_status is not None:
            self.invoice_status = invoice_status
        if sub_total is not None:
            self.sub_total = sub_total
        if tax is not None:
            self.tax = tax
        if tax_percent is not None:
            self.tax_percent = tax_percent
        if total is not None:
            self.total = total

    @property
    def items(self):
        """Gets the items of this InvoiceOut.  # noqa: E501


        :return: The items of this InvoiceOut.  # noqa: E501
        :rtype: list[InvoiceItemOut]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this InvoiceOut.


        :param items: The items of this InvoiceOut.  # noqa: E501
        :type: list[InvoiceItemOut]
        """

        self._items = items

    @property
    def user_id(self):
        """Gets the user_id of this InvoiceOut.  # noqa: E501


        :return: The user_id of this InvoiceOut.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this InvoiceOut.


        :param user_id: The user_id of this InvoiceOut.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def invoice_id(self):
        """Gets the invoice_id of this InvoiceOut.  # noqa: E501


        :return: The invoice_id of this InvoiceOut.  # noqa: E501
        :rtype: str
        """
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id):
        """Sets the invoice_id of this InvoiceOut.


        :param invoice_id: The invoice_id of this InvoiceOut.  # noqa: E501
        :type: str
        """

        self._invoice_id = invoice_id

    @property
    def is_striped(self):
        """Gets the is_striped of this InvoiceOut.  # noqa: E501


        :return: The is_striped of this InvoiceOut.  # noqa: E501
        :rtype: bool
        """
        return self._is_striped

    @is_striped.setter
    def is_striped(self, is_striped):
        """Sets the is_striped of this InvoiceOut.


        :param is_striped: The is_striped of this InvoiceOut.  # noqa: E501
        :type: bool
        """

        self._is_striped = is_striped

    @property
    def stripe_customer_id(self):
        """Gets the stripe_customer_id of this InvoiceOut.  # noqa: E501


        :return: The stripe_customer_id of this InvoiceOut.  # noqa: E501
        :rtype: str
        """
        return self._stripe_customer_id

    @stripe_customer_id.setter
    def stripe_customer_id(self, stripe_customer_id):
        """Sets the stripe_customer_id of this InvoiceOut.


        :param stripe_customer_id: The stripe_customer_id of this InvoiceOut.  # noqa: E501
        :type: str
        """

        self._stripe_customer_id = stripe_customer_id

    @property
    def amount_due(self):
        """Gets the amount_due of this InvoiceOut.  # noqa: E501


        :return: The amount_due of this InvoiceOut.  # noqa: E501
        :rtype: int
        """
        return self._amount_due

    @amount_due.setter
    def amount_due(self, amount_due):
        """Sets the amount_due of this InvoiceOut.


        :param amount_due: The amount_due of this InvoiceOut.  # noqa: E501
        :type: int
        """

        self._amount_due = amount_due

    @property
    def amount_paid(self):
        """Gets the amount_paid of this InvoiceOut.  # noqa: E501


        :return: The amount_paid of this InvoiceOut.  # noqa: E501
        :rtype: int
        """
        return self._amount_paid

    @amount_paid.setter
    def amount_paid(self, amount_paid):
        """Sets the amount_paid of this InvoiceOut.


        :param amount_paid: The amount_paid of this InvoiceOut.  # noqa: E501
        :type: int
        """

        self._amount_paid = amount_paid

    @property
    def amount_remaining(self):
        """Gets the amount_remaining of this InvoiceOut.  # noqa: E501


        :return: The amount_remaining of this InvoiceOut.  # noqa: E501
        :rtype: int
        """
        return self._amount_remaining

    @amount_remaining.setter
    def amount_remaining(self, amount_remaining):
        """Sets the amount_remaining of this InvoiceOut.


        :param amount_remaining: The amount_remaining of this InvoiceOut.  # noqa: E501
        :type: int
        """

        self._amount_remaining = amount_remaining

    @property
    def attempted(self):
        """Gets the attempted of this InvoiceOut.  # noqa: E501


        :return: The attempted of this InvoiceOut.  # noqa: E501
        :rtype: bool
        """
        return self._attempted

    @attempted.setter
    def attempted(self, attempted):
        """Sets the attempted of this InvoiceOut.


        :param attempted: The attempted of this InvoiceOut.  # noqa: E501
        :type: bool
        """

        self._attempted = attempted

    @property
    def currency(self):
        """Gets the currency of this InvoiceOut.  # noqa: E501


        :return: The currency of this InvoiceOut.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this InvoiceOut.


        :param currency: The currency of this InvoiceOut.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def invoice_date(self):
        """Gets the invoice_date of this InvoiceOut.  # noqa: E501


        :return: The invoice_date of this InvoiceOut.  # noqa: E501
        :rtype: datetime
        """
        return self._invoice_date

    @invoice_date.setter
    def invoice_date(self, invoice_date):
        """Sets the invoice_date of this InvoiceOut.


        :param invoice_date: The invoice_date of this InvoiceOut.  # noqa: E501
        :type: datetime
        """

        self._invoice_date = invoice_date

    @property
    def due_date(self):
        """Gets the due_date of this InvoiceOut.  # noqa: E501


        :return: The due_date of this InvoiceOut.  # noqa: E501
        :rtype: datetime
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this InvoiceOut.


        :param due_date: The due_date of this InvoiceOut.  # noqa: E501
        :type: datetime
        """

        self._due_date = due_date

    @property
    def description(self):
        """Gets the description of this InvoiceOut.  # noqa: E501


        :return: The description of this InvoiceOut.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InvoiceOut.


        :param description: The description of this InvoiceOut.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def invoice_pdf(self):
        """Gets the invoice_pdf of this InvoiceOut.  # noqa: E501


        :return: The invoice_pdf of this InvoiceOut.  # noqa: E501
        :rtype: str
        """
        return self._invoice_pdf

    @invoice_pdf.setter
    def invoice_pdf(self, invoice_pdf):
        """Sets the invoice_pdf of this InvoiceOut.


        :param invoice_pdf: The invoice_pdf of this InvoiceOut.  # noqa: E501
        :type: str
        """

        self._invoice_pdf = invoice_pdf

    @property
    def period_start(self):
        """Gets the period_start of this InvoiceOut.  # noqa: E501


        :return: The period_start of this InvoiceOut.  # noqa: E501
        :rtype: datetime
        """
        return self._period_start

    @period_start.setter
    def period_start(self, period_start):
        """Sets the period_start of this InvoiceOut.


        :param period_start: The period_start of this InvoiceOut.  # noqa: E501
        :type: datetime
        """

        self._period_start = period_start

    @property
    def period_end(self):
        """Gets the period_end of this InvoiceOut.  # noqa: E501


        :return: The period_end of this InvoiceOut.  # noqa: E501
        :rtype: datetime
        """
        return self._period_end

    @period_end.setter
    def period_end(self, period_end):
        """Sets the period_end of this InvoiceOut.


        :param period_end: The period_end of this InvoiceOut.  # noqa: E501
        :type: datetime
        """

        self._period_end = period_end

    @property
    def receipt_number(self):
        """Gets the receipt_number of this InvoiceOut.  # noqa: E501


        :return: The receipt_number of this InvoiceOut.  # noqa: E501
        :rtype: str
        """
        return self._receipt_number

    @receipt_number.setter
    def receipt_number(self, receipt_number):
        """Sets the receipt_number of this InvoiceOut.


        :param receipt_number: The receipt_number of this InvoiceOut.  # noqa: E501
        :type: str
        """

        self._receipt_number = receipt_number

    @property
    def invoice_status(self):
        """Gets the invoice_status of this InvoiceOut.  # noqa: E501


        :return: The invoice_status of this InvoiceOut.  # noqa: E501
        :rtype: str
        """
        return self._invoice_status

    @invoice_status.setter
    def invoice_status(self, invoice_status):
        """Sets the invoice_status of this InvoiceOut.


        :param invoice_status: The invoice_status of this InvoiceOut.  # noqa: E501
        :type: str
        """

        self._invoice_status = invoice_status

    @property
    def sub_total(self):
        """Gets the sub_total of this InvoiceOut.  # noqa: E501


        :return: The sub_total of this InvoiceOut.  # noqa: E501
        :rtype: int
        """
        return self._sub_total

    @sub_total.setter
    def sub_total(self, sub_total):
        """Sets the sub_total of this InvoiceOut.


        :param sub_total: The sub_total of this InvoiceOut.  # noqa: E501
        :type: int
        """

        self._sub_total = sub_total

    @property
    def tax(self):
        """Gets the tax of this InvoiceOut.  # noqa: E501


        :return: The tax of this InvoiceOut.  # noqa: E501
        :rtype: int
        """
        return self._tax

    @tax.setter
    def tax(self, tax):
        """Sets the tax of this InvoiceOut.


        :param tax: The tax of this InvoiceOut.  # noqa: E501
        :type: int
        """

        self._tax = tax

    @property
    def tax_percent(self):
        """Gets the tax_percent of this InvoiceOut.  # noqa: E501


        :return: The tax_percent of this InvoiceOut.  # noqa: E501
        :rtype: int
        """
        return self._tax_percent

    @tax_percent.setter
    def tax_percent(self, tax_percent):
        """Sets the tax_percent of this InvoiceOut.


        :param tax_percent: The tax_percent of this InvoiceOut.  # noqa: E501
        :type: int
        """

        self._tax_percent = tax_percent

    @property
    def total(self):
        """Gets the total of this InvoiceOut.  # noqa: E501


        :return: The total of this InvoiceOut.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this InvoiceOut.


        :param total: The total of this InvoiceOut.  # noqa: E501
        :type: int
        """

        self._total = total

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
        if not isinstance(other, InvoiceOut):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
