# coding: utf-8

"""
    BitMEX API

    REST API for the BitMEX.com trading platform.<br><br><a href=\"/app/restAPI\">REST Documentation</a><br><a href=\"/app/wsAPI\">Websocket Documentation</a>

    OpenAPI spec version: 1.2.0
    Contact: support@bitmex.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class ChatApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def chat_get(self, **kwargs):
        """
        Get chat messages.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.chat_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param float count: Number of results to fetch.
        :param float start: Starting point for results.
        :param bool reverse: If true, will sort results newest first.
        :return: list[Chat]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.chat_get_with_http_info(**kwargs)
        else:
            (data) = self.chat_get_with_http_info(**kwargs)
            return data

    def chat_get_with_http_info(self, **kwargs):
        """
        Get chat messages.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.chat_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param float count: Number of results to fetch.
        :param float start: Starting point for results.
        :param bool reverse: If true, will sort results newest first.
        :return: list[Chat]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['count', 'start', 'reverse']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method chat_get" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/chat'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'count' in params:
            query_params['count'] = params['count']
        if 'start' in params:
            query_params['start'] = params['start']
        if 'reverse' in params:
            query_params['reverse'] = params['reverse']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'application/xml', 'text/xml', 'application/javascript', 'text/javascript'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[Chat]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def chat_get_connected(self, **kwargs):
        """
        Get connected users.
        Returns an array with browser users in the first position and API users (bots) in the second position.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.chat_get_connected(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: ConnectedUsers
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.chat_get_connected_with_http_info(**kwargs)
        else:
            (data) = self.chat_get_connected_with_http_info(**kwargs)
            return data

    def chat_get_connected_with_http_info(self, **kwargs):
        """
        Get connected users.
        Returns an array with browser users in the first position and API users (bots) in the second position.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.chat_get_connected_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: ConnectedUsers
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method chat_get_connected" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/chat/connected'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'application/xml', 'text/xml', 'application/javascript', 'text/javascript'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='ConnectedUsers',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def chat_new(self, message, **kwargs):
        """
        Send a chat message.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.chat_new(message, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str message:  (required)
        :return: Chat
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.chat_new_with_http_info(message, **kwargs)
        else:
            (data) = self.chat_new_with_http_info(message, **kwargs)
            return data

    def chat_new_with_http_info(self, message, **kwargs):
        """
        Send a chat message.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.chat_new_with_http_info(message, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str message:  (required)
        :return: Chat
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['message']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method chat_new" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'message' is set
        if ('message' not in params) or (params['message'] is None):
            raise ValueError("Missing the required parameter `message` when calling `chat_new`")

        if 'message' in params and params['message'] > 500.0:
            raise ValueError("Invalid value for parameter `message` when calling `chat_new`, must be a value less than or equal to  `500.0`")
        resource_path = '/chat'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'message' in params:
            form_params.append(('message', params['message']))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'application/xml', 'text/xml', 'application/javascript', 'text/javascript'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='Chat',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))