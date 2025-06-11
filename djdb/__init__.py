# -*- encoding: utf-8 -*-
'''
@File    :   __init__.py
@Time    :   2025/06/11 19:47:17
@Author  :   xzy 
@Version :   1.0
@Contact :   1580987871@qq.com
'''

# here put the import lib

try:
    import os
    import django
    from django.conf import settings
except ImportError:
    raise ImportError("Couldn't import Django. Are you sure it's installed and "
                      "available on your PYTHONPATH environment variable? Did you "
                      "forget to activate a virtual environment?")


def _setup():
    if not settings.configured:
        import pymysql
        pymysql.install_as_MySQLdb()
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'djdb.settings')
        django.setup()


_setup()

del _setup
