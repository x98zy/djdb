# -*- encoding: utf-8 -*-
'''
@File    :   lazyobject.py
@Time    :   2025/06/14 16:25:14
@Author  :   xzy 
@Version :   1.0
@Contact :   1580987871@qq.com
'''

# here put the import lib
import importlib
import typing

from django.utils.functional import SimpleLazyObject

if typing.TYPE_CHECKING:
    from django_redis.cache import RedisCache


cache = SimpleLazyObject(lambda: importlib.import_module(
    'django.core.cache').caches['default'])  # type: RedisCache
