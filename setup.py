# -*- encoding: utf-8 -*-
'''
@File    :   setup.py
@Time    :   2025/06/11 20:37:48
@Author  :   xzy 
@Version :   1.0
@Contact :   1580987871@qq.com
'''

# here put the import lib
from setuptools import setup


def parse_requirements(filename):
    with open(filename, encoding='utf-8-sig') as f:
        lines = f.read().splitlines()
        # 去掉空行和注释行
        return [line for line in lines if line.strip() and not line.startswith("#")]


setup(
    name="djdb",
    version="1.0.0",
    author="xzy",
    author_email="1580987871@qq.com",
    description="Django ORM独立库, 可以不同进程使用",
    packages=['djdb'],
    install_requires=parse_requirements("requirements.txt"),
    entry_points={
        'console_scripts': [
            'djdb = djdb.command:main',
        ]
    }
)
