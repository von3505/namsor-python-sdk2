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


class APIKeyOut(object):
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
        'api_key': 'str',
        'user_id': 'str',
        'admin': 'bool',
        'vetted': 'bool',
        'learnable': 'bool',
        'anonymized': 'bool',
        'partner': 'bool',
        'striped': 'bool',
        'corporate': 'bool',
        'disabled': 'bool'
    }

    attribute_map = {
        'api_key': 'apiKey',
        'user_id': 'userId',
        'admin': 'admin',
        'vetted': 'vetted',
        'learnable': 'learnable',
        'anonymized': 'anonymized',
        'partner': 'partner',
        'striped': 'striped',
        'corporate': 'corporate',
        'disabled': 'disabled'
    }

    def __init__(self, api_key=None, user_id=None, admin=None, vetted=None, learnable=None, anonymized=None, partner=None, striped=None, corporate=None, disabled=None):  # noqa: E501
        """APIKeyOut - a model defined in OpenAPI"""  # noqa: E501

        self._api_key = None
        self._user_id = None
        self._admin = None
        self._vetted = None
        self._learnable = None
        self._anonymized = None
        self._partner = None
        self._striped = None
        self._corporate = None
        self._disabled = None
        self.discriminator = None

        if api_key is not None:
            self.api_key = api_key
        if user_id is not None:
            self.user_id = user_id
        if admin is not None:
            self.admin = admin
        if vetted is not None:
            self.vetted = vetted
        if learnable is not None:
            self.learnable = learnable
        if anonymized is not None:
            self.anonymized = anonymized
        if partner is not None:
            self.partner = partner
        if striped is not None:
            self.striped = striped
        if corporate is not None:
            self.corporate = corporate
        if disabled is not None:
            self.disabled = disabled

    @property
    def api_key(self):
        """Gets the api_key of this APIKeyOut.  # noqa: E501


        :return: The api_key of this APIKeyOut.  # noqa: E501
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """Sets the api_key of this APIKeyOut.


        :param api_key: The api_key of this APIKeyOut.  # noqa: E501
        :type: str
        """

        self._api_key = api_key

    @property
    def user_id(self):
        """Gets the user_id of this APIKeyOut.  # noqa: E501


        :return: The user_id of this APIKeyOut.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this APIKeyOut.


        :param user_id: The user_id of this APIKeyOut.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def admin(self):
        """Gets the admin of this APIKeyOut.  # noqa: E501


        :return: The admin of this APIKeyOut.  # noqa: E501
        :rtype: bool
        """
        return self._admin

    @admin.setter
    def admin(self, admin):
        """Sets the admin of this APIKeyOut.


        :param admin: The admin of this APIKeyOut.  # noqa: E501
        :type: bool
        """

        self._admin = admin

    @property
    def vetted(self):
        """Gets the vetted of this APIKeyOut.  # noqa: E501


        :return: The vetted of this APIKeyOut.  # noqa: E501
        :rtype: bool
        """
        return self._vetted

    @vetted.setter
    def vetted(self, vetted):
        """Sets the vetted of this APIKeyOut.


        :param vetted: The vetted of this APIKeyOut.  # noqa: E501
        :type: bool
        """

        self._vetted = vetted

    @property
    def learnable(self):
        """Gets the learnable of this APIKeyOut.  # noqa: E501


        :return: The learnable of this APIKeyOut.  # noqa: E501
        :rtype: bool
        """
        return self._learnable

    @learnable.setter
    def learnable(self, learnable):
        """Sets the learnable of this APIKeyOut.


        :param learnable: The learnable of this APIKeyOut.  # noqa: E501
        :type: bool
        """

        self._learnable = learnable

    @property
    def anonymized(self):
        """Gets the anonymized of this APIKeyOut.  # noqa: E501


        :return: The anonymized of this APIKeyOut.  # noqa: E501
        :rtype: bool
        """
        return self._anonymized

    @anonymized.setter
    def anonymized(self, anonymized):
        """Sets the anonymized of this APIKeyOut.


        :param anonymized: The anonymized of this APIKeyOut.  # noqa: E501
        :type: bool
        """

        self._anonymized = anonymized

    @property
    def partner(self):
        """Gets the partner of this APIKeyOut.  # noqa: E501


        :return: The partner of this APIKeyOut.  # noqa: E501
        :rtype: bool
        """
        return self._partner

    @partner.setter
    def partner(self, partner):
        """Sets the partner of this APIKeyOut.


        :param partner: The partner of this APIKeyOut.  # noqa: E501
        :type: bool
        """

        self._partner = partner

    @property
    def striped(self):
        """Gets the striped of this APIKeyOut.  # noqa: E501


        :return: The striped of this APIKeyOut.  # noqa: E501
        :rtype: bool
        """
        return self._striped

    @striped.setter
    def striped(self, striped):
        """Sets the striped of this APIKeyOut.


        :param striped: The striped of this APIKeyOut.  # noqa: E501
        :type: bool
        """

        self._striped = striped

    @property
    def corporate(self):
        """Gets the corporate of this APIKeyOut.  # noqa: E501


        :return: The corporate of this APIKeyOut.  # noqa: E501
        :rtype: bool
        """
        return self._corporate

    @corporate.setter
    def corporate(self, corporate):
        """Sets the corporate of this APIKeyOut.


        :param corporate: The corporate of this APIKeyOut.  # noqa: E501
        :type: bool
        """

        self._corporate = corporate

    @property
    def disabled(self):
        """Gets the disabled of this APIKeyOut.  # noqa: E501


        :return: The disabled of this APIKeyOut.  # noqa: E501
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this APIKeyOut.


        :param disabled: The disabled of this APIKeyOut.  # noqa: E501
        :type: bool
        """

        self._disabled = disabled

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
        if not isinstance(other, APIKeyOut):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
