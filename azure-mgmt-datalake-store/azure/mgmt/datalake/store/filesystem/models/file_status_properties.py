# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class FileStatusProperties(Model):
    """Data Lake Store file or directory information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar access_time: the last access time as ticks since the epoch.
    :vartype access_time: long
    :ivar block_size: the block size for the file.
    :vartype block_size: long
    :ivar children_num: the number of children in the directory.
    :vartype children_num: long
    :ivar group: the group owner.
    :vartype group: str
    :ivar length: the number of bytes in a file.
    :vartype length: long
    :ivar modification_time: the modification time as ticks since the epoch.
    :vartype modification_time: long
    :ivar owner: the user who is the owner.
    :vartype owner: str
    :ivar path_suffix: the path suffix.
    :vartype path_suffix: str
    :ivar permission: the permission represented as an string.
    :vartype permission: str
    :ivar type: the type of the path object. Possible values include: 'FILE',
     'DIRECTORY'
    :vartype type: str or :class:`FileType
     <azure.mgmt.datalake.store.filesystem.models.FileType>`
    """ 

    _validation = {
        'access_time': {'readonly': True},
        'block_size': {'readonly': True},
        'children_num': {'readonly': True},
        'group': {'readonly': True},
        'length': {'readonly': True},
        'modification_time': {'readonly': True},
        'owner': {'readonly': True},
        'path_suffix': {'readonly': True},
        'permission': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'access_time': {'key': 'accessTime', 'type': 'long'},
        'block_size': {'key': 'blockSize', 'type': 'long'},
        'children_num': {'key': 'childrenNum', 'type': 'long'},
        'group': {'key': 'group', 'type': 'str'},
        'length': {'key': 'length', 'type': 'long'},
        'modification_time': {'key': 'modificationTime', 'type': 'long'},
        'owner': {'key': 'owner', 'type': 'str'},
        'path_suffix': {'key': 'pathSuffix', 'type': 'str'},
        'permission': {'key': 'permission', 'type': 'str'},
        'type': {'key': 'type', 'type': 'FileType'},
    }

    def __init__(self):
        self.access_time = None
        self.block_size = None
        self.children_num = None
        self.group = None
        self.length = None
        self.modification_time = None
        self.owner = None
        self.path_suffix = None
        self.permission = None
        self.type = None
