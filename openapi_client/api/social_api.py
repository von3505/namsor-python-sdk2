# coding: utf-8

"""
    NamSor API v2

    NamSor API v2 : enpoints to process personal names (gender, cultural origin or ethnicity) in all alphabets or languages. Use GET methods for small tests, but prefer POST methods for higher throughput (batch processing of up to 100 names at a time). Need something you can't find here? We have many more features coming soon. Let us know, we'll do our best to add it!   # noqa: E501

    OpenAPI spec version: 2.0.7
    Contact: contact@namsor.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openapi_client.api_client import ApiClient


class SocialApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def phone_code(self, first_name, last_name, phone_number, **kwargs):  # noqa: E501
        """[USES 11 UNITS] Infer the likely country and phone prefix, given a personal name and formatted / unformatted phone number.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.phone_code(first_name, last_name, phone_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str first_name: (required)
        :param str last_name: (required)
        :param str phone_number: (required)
        :return: FirstLastNamePhoneCodedOut
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.phone_code_with_http_info(first_name, last_name, phone_number, **kwargs)  # noqa: E501
        else:
            (data) = self.phone_code_with_http_info(first_name, last_name, phone_number, **kwargs)  # noqa: E501
            return data

    def phone_code_with_http_info(self, first_name, last_name, phone_number, **kwargs):  # noqa: E501
        """[USES 11 UNITS] Infer the likely country and phone prefix, given a personal name and formatted / unformatted phone number.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.phone_code_with_http_info(first_name, last_name, phone_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str first_name: (required)
        :param str last_name: (required)
        :param str phone_number: (required)
        :return: FirstLastNamePhoneCodedOut
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['first_name', 'last_name', 'phone_number']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method phone_code" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'first_name' is set
        if ('first_name' not in local_var_params or
                local_var_params['first_name'] is None):
            raise ValueError("Missing the required parameter `first_name` when calling `phone_code`")  # noqa: E501
        # verify the required parameter 'last_name' is set
        if ('last_name' not in local_var_params or
                local_var_params['last_name'] is None):
            raise ValueError("Missing the required parameter `last_name` when calling `phone_code`")  # noqa: E501
        # verify the required parameter 'phone_number' is set
        if ('phone_number' not in local_var_params or
                local_var_params['phone_number'] is None):
            raise ValueError("Missing the required parameter `phone_number` when calling `phone_code`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'first_name' in local_var_params:
            path_params['firstName'] = local_var_params['first_name']  # noqa: E501
        if 'last_name' in local_var_params:
            path_params['lastName'] = local_var_params['last_name']  # noqa: E501
        if 'phone_number' in local_var_params:
            path_params['phoneNumber'] = local_var_params['phone_number']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/api2/json/phoneCode/{firstName}/{lastName}/{phoneNumber}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FirstLastNamePhoneCodedOut',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def phone_code_batch(self, **kwargs):  # noqa: E501
        """[USES 11 UNITS] Infer the likely country and phone prefix, of up to 100 personal names, detecting automatically the local context given a name and formatted / unformatted phone number.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.phone_code_batch(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BatchFirstLastNamePhoneNumberIn batch_first_last_name_phone_number_in: A list of personal names
        :return: BatchFirstLastNamePhoneCodedOut
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.phone_code_batch_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.phone_code_batch_with_http_info(**kwargs)  # noqa: E501
            return data

    def phone_code_batch_with_http_info(self, **kwargs):  # noqa: E501
        """[USES 11 UNITS] Infer the likely country and phone prefix, of up to 100 personal names, detecting automatically the local context given a name and formatted / unformatted phone number.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.phone_code_batch_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BatchFirstLastNamePhoneNumberIn batch_first_last_name_phone_number_in: A list of personal names
        :return: BatchFirstLastNamePhoneCodedOut
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['batch_first_last_name_phone_number_in']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method phone_code_batch" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'batch_first_last_name_phone_number_in' in local_var_params:
            body_params = local_var_params['batch_first_last_name_phone_number_in']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/api2/json/phoneCodeBatch', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BatchFirstLastNamePhoneCodedOut',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def phone_code_geo(self, first_name, last_name, phone_number, country_iso2, **kwargs):  # noqa: E501
        """[USES 11 UNITS] Infer the likely phone prefix, given a personal name and formatted / unformatted phone number, with a local context (ISO2 country of residence).  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.phone_code_geo(first_name, last_name, phone_number, country_iso2, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str first_name: (required)
        :param str last_name: (required)
        :param str phone_number: (required)
        :param str country_iso2: (required)
        :return: FirstLastNamePhoneCodedOut
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.phone_code_geo_with_http_info(first_name, last_name, phone_number, country_iso2, **kwargs)  # noqa: E501
        else:
            (data) = self.phone_code_geo_with_http_info(first_name, last_name, phone_number, country_iso2, **kwargs)  # noqa: E501
            return data

    def phone_code_geo_with_http_info(self, first_name, last_name, phone_number, country_iso2, **kwargs):  # noqa: E501
        """[USES 11 UNITS] Infer the likely phone prefix, given a personal name and formatted / unformatted phone number, with a local context (ISO2 country of residence).  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.phone_code_geo_with_http_info(first_name, last_name, phone_number, country_iso2, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str first_name: (required)
        :param str last_name: (required)
        :param str phone_number: (required)
        :param str country_iso2: (required)
        :return: FirstLastNamePhoneCodedOut
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['first_name', 'last_name', 'phone_number', 'country_iso2']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method phone_code_geo" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'first_name' is set
        if ('first_name' not in local_var_params or
                local_var_params['first_name'] is None):
            raise ValueError("Missing the required parameter `first_name` when calling `phone_code_geo`")  # noqa: E501
        # verify the required parameter 'last_name' is set
        if ('last_name' not in local_var_params or
                local_var_params['last_name'] is None):
            raise ValueError("Missing the required parameter `last_name` when calling `phone_code_geo`")  # noqa: E501
        # verify the required parameter 'phone_number' is set
        if ('phone_number' not in local_var_params or
                local_var_params['phone_number'] is None):
            raise ValueError("Missing the required parameter `phone_number` when calling `phone_code_geo`")  # noqa: E501
        # verify the required parameter 'country_iso2' is set
        if ('country_iso2' not in local_var_params or
                local_var_params['country_iso2'] is None):
            raise ValueError("Missing the required parameter `country_iso2` when calling `phone_code_geo`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'first_name' in local_var_params:
            path_params['firstName'] = local_var_params['first_name']  # noqa: E501
        if 'last_name' in local_var_params:
            path_params['lastName'] = local_var_params['last_name']  # noqa: E501
        if 'phone_number' in local_var_params:
            path_params['phoneNumber'] = local_var_params['phone_number']  # noqa: E501
        if 'country_iso2' in local_var_params:
            path_params['countryIso2'] = local_var_params['country_iso2']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/api2/json/phoneCodeGeo/{firstName}/{lastName}/{phoneNumber}/{countryIso2}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FirstLastNamePhoneCodedOut',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def phone_code_geo_batch(self, **kwargs):  # noqa: E501
        """[USES 11 UNITS] Infer the likely country and phone prefix, of up to 100 personal names, with a local context (ISO2 country of residence).  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.phone_code_geo_batch(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BatchFirstLastNamePhoneNumberGeoIn batch_first_last_name_phone_number_geo_in: A list of personal names
        :return: BatchFirstLastNamePhoneCodedOut
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.phone_code_geo_batch_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.phone_code_geo_batch_with_http_info(**kwargs)  # noqa: E501
            return data

    def phone_code_geo_batch_with_http_info(self, **kwargs):  # noqa: E501
        """[USES 11 UNITS] Infer the likely country and phone prefix, of up to 100 personal names, with a local context (ISO2 country of residence).  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.phone_code_geo_batch_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BatchFirstLastNamePhoneNumberGeoIn batch_first_last_name_phone_number_geo_in: A list of personal names
        :return: BatchFirstLastNamePhoneCodedOut
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['batch_first_last_name_phone_number_geo_in']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method phone_code_geo_batch" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'batch_first_last_name_phone_number_geo_in' in local_var_params:
            body_params = local_var_params['batch_first_last_name_phone_number_geo_in']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/api2/json/phoneCodeGeoBatch', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BatchFirstLastNamePhoneCodedOut',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def phone_code_geo_feedback_loop(self, first_name, last_name, phone_number, phone_number_e164, country_iso2, **kwargs):  # noqa: E501
        """[CREDITS 1 UNIT] Feedback loop to better infer the likely phone prefix, given a personal name and formatted / unformatted phone number, with a local context (ISO2 country of residence).  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.phone_code_geo_feedback_loop(first_name, last_name, phone_number, phone_number_e164, country_iso2, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str first_name: (required)
        :param str last_name: (required)
        :param str phone_number: (required)
        :param str phone_number_e164: (required)
        :param str country_iso2: (required)
        :return: FirstLastNamePhoneCodedOut
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.phone_code_geo_feedback_loop_with_http_info(first_name, last_name, phone_number, phone_number_e164, country_iso2, **kwargs)  # noqa: E501
        else:
            (data) = self.phone_code_geo_feedback_loop_with_http_info(first_name, last_name, phone_number, phone_number_e164, country_iso2, **kwargs)  # noqa: E501
            return data

    def phone_code_geo_feedback_loop_with_http_info(self, first_name, last_name, phone_number, phone_number_e164, country_iso2, **kwargs):  # noqa: E501
        """[CREDITS 1 UNIT] Feedback loop to better infer the likely phone prefix, given a personal name and formatted / unformatted phone number, with a local context (ISO2 country of residence).  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.phone_code_geo_feedback_loop_with_http_info(first_name, last_name, phone_number, phone_number_e164, country_iso2, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str first_name: (required)
        :param str last_name: (required)
        :param str phone_number: (required)
        :param str phone_number_e164: (required)
        :param str country_iso2: (required)
        :return: FirstLastNamePhoneCodedOut
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['first_name', 'last_name', 'phone_number', 'phone_number_e164', 'country_iso2']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method phone_code_geo_feedback_loop" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'first_name' is set
        if ('first_name' not in local_var_params or
                local_var_params['first_name'] is None):
            raise ValueError("Missing the required parameter `first_name` when calling `phone_code_geo_feedback_loop`")  # noqa: E501
        # verify the required parameter 'last_name' is set
        if ('last_name' not in local_var_params or
                local_var_params['last_name'] is None):
            raise ValueError("Missing the required parameter `last_name` when calling `phone_code_geo_feedback_loop`")  # noqa: E501
        # verify the required parameter 'phone_number' is set
        if ('phone_number' not in local_var_params or
                local_var_params['phone_number'] is None):
            raise ValueError("Missing the required parameter `phone_number` when calling `phone_code_geo_feedback_loop`")  # noqa: E501
        # verify the required parameter 'phone_number_e164' is set
        if ('phone_number_e164' not in local_var_params or
                local_var_params['phone_number_e164'] is None):
            raise ValueError("Missing the required parameter `phone_number_e164` when calling `phone_code_geo_feedback_loop`")  # noqa: E501
        # verify the required parameter 'country_iso2' is set
        if ('country_iso2' not in local_var_params or
                local_var_params['country_iso2'] is None):
            raise ValueError("Missing the required parameter `country_iso2` when calling `phone_code_geo_feedback_loop`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'first_name' in local_var_params:
            path_params['firstName'] = local_var_params['first_name']  # noqa: E501
        if 'last_name' in local_var_params:
            path_params['lastName'] = local_var_params['last_name']  # noqa: E501
        if 'phone_number' in local_var_params:
            path_params['phoneNumber'] = local_var_params['phone_number']  # noqa: E501
        if 'phone_number_e164' in local_var_params:
            path_params['phoneNumberE164'] = local_var_params['phone_number_e164']  # noqa: E501
        if 'country_iso2' in local_var_params:
            path_params['countryIso2'] = local_var_params['country_iso2']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/api2/json/phoneCodeGeoFeedbackLoop/{firstName}/{lastName}/{phoneNumber}/{phoneNumberE164}/{countryIso2}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FirstLastNamePhoneCodedOut',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
