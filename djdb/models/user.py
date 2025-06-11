# -*- encoding: utf-8 -*-
'''
@File    :   user.py
@Time    :   2025/06/11 21:20:20
@Author  :   xzy 
@Version :   1.0
@Contact :   1580987871@qq.com
'''

# here put the import lib
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # 添加自定义字段
    age = models.PositiveIntegerField(null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)

    # 添加自定义方法
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
