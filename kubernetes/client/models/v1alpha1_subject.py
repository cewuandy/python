# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.5.1
    
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

from pprint import pformat
from six import iteritems
import re


class V1alpha1Subject(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, api_version=None, kind=None, name=None, namespace=None):
        """
        V1alpha1Subject - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'api_version': 'str',
            'kind': 'str',
            'name': 'str',
            'namespace': 'str'
        }

        self.attribute_map = {
            'api_version': 'apiVersion',
            'kind': 'kind',
            'name': 'name',
            'namespace': 'namespace'
        }

        self._api_version = api_version
        self._kind = kind
        self._name = name
        self._namespace = namespace


    @property
    def api_version(self):
        """
        Gets the api_version of this V1alpha1Subject.
        APIVersion holds the API group and version of the referenced object.

        :return: The api_version of this V1alpha1Subject.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """
        Sets the api_version of this V1alpha1Subject.
        APIVersion holds the API group and version of the referenced object.

        :param api_version: The api_version of this V1alpha1Subject.
        :type: str
        """

        self._api_version = api_version

    @property
    def kind(self):
        """
        Gets the kind of this V1alpha1Subject.
        Kind of object being referenced. Values defined by this API group are \"User\", \"Group\", and \"ServiceAccount\". If the Authorizer does not recognized the kind value, the Authorizer should report an error.

        :return: The kind of this V1alpha1Subject.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1alpha1Subject.
        Kind of object being referenced. Values defined by this API group are \"User\", \"Group\", and \"ServiceAccount\". If the Authorizer does not recognized the kind value, the Authorizer should report an error.

        :param kind: The kind of this V1alpha1Subject.
        :type: str
        """
        if kind is None:
            raise ValueError("Invalid value for `kind`, must not be `None`")

        self._kind = kind

    @property
    def name(self):
        """
        Gets the name of this V1alpha1Subject.
        Name of the object being referenced.

        :return: The name of this V1alpha1Subject.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1alpha1Subject.
        Name of the object being referenced.

        :param name: The name of this V1alpha1Subject.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def namespace(self):
        """
        Gets the namespace of this V1alpha1Subject.
        Namespace of the referenced object.  If the object kind is non-namespace, such as \"User\" or \"Group\", and this value is not empty the Authorizer should report an error.

        :return: The namespace of this V1alpha1Subject.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this V1alpha1Subject.
        Namespace of the referenced object.  If the object kind is non-namespace, such as \"User\" or \"Group\", and this value is not empty the Authorizer should report an error.

        :param namespace: The namespace of this V1alpha1Subject.
        :type: str
        """

        self._namespace = namespace

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
