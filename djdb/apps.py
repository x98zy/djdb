# -*- encoding: utf-8 -*-
'''
@File    :   apps.py
@Time    :   2025/06/11 20:53:31
@Author  :   xzy 
@Version :   1.0
@Contact :   1580987871@qq.com
'''

# here put the import lib
import os

from django.apps import AppConfig
from importlib import import_module


class App(AppConfig):
    name = 'djdb'

    def import_models(self) -> None:
        if self.module:
            package_dir = self.module.__path__[0] if len(
                self.module.__path__) >= 1 else None
            if package_dir:
                for name, dir, files in os.walk(os.path.join(package_dir, "models")):
                    for file in files:
                        if file.startswith("__init__") or not file.endswith("py"):
                            continue
                        prefix = file.partition(".")[0]
                        submodule = "djdb.models.%s" % prefix
                        import_module(submodule)

        super().import_models()
