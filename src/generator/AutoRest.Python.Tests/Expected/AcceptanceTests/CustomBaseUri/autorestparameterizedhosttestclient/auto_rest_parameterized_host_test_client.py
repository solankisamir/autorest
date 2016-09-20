# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import ServiceClient
from msrest import Configuration, Serializer, Deserializer
from .version import VERSION
from .operations.paths_operations import PathsOperations
from . import models


class AutoRestParameterizedHostTestClientConfiguration(Configuration):
    """Configuration for AutoRestParameterizedHostTestClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param host: A string value that is used as a global part of the
     parameterized host
    :type host: str
    :param str filepath: Existing config
    """

    def __init__(
            self, host, filepath=None):

        if host is None:
            raise ValueError("Parameter 'host' must not be None.")
        if not isinstance(host, str):
            raise TypeError("Parameter 'host' must be str.")
        base_url = 'http://{accountName}{host}'

        super(AutoRestParameterizedHostTestClientConfiguration, self).__init__(base_url, filepath)

        self.add_user_agent('autorestparameterizedhosttestclient/{}'.format(VERSION))

        self.host = host


class AutoRestParameterizedHostTestClient(object):
    """Test Infrastructure for AutoRest

    :ivar config: Configuration for client.
    :vartype config: AutoRestParameterizedHostTestClientConfiguration

    :ivar paths: Paths operations
    :vartype paths: .operations.PathsOperations

    :param host: A string value that is used as a global part of the
     parameterized host
    :type host: str
    :param str filepath: Existing config
    """

    def __init__(
            self, host, filepath=None):

        self.config = AutoRestParameterizedHostTestClientConfiguration(host, filepath)
        self._client = ServiceClient(None, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.paths = PathsOperations(
            self._client, self.config, self._serialize, self._deserialize)
