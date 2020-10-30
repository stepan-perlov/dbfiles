#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import setup
from dbfiles import __version__

setup(
    name="dbfiles",
    version=__version__,
    description="dbfiles - util for compile you sql files, csv data files, yaml, json configuration into catalog of sql files",
    license='MIT',
    author="Stepan Perlov",
    author_email="stepanperlov@gmail.com",
    install_requires=[
        "PyYAML",
        "jsonschema",
    ],
    packages=[
        "dbfiles",
        "dbfiles.items"
    ],
    entry_points={
        "console_scripts": [
            "dbfiles = dbfiles.main:main",
        ]
    },
    package_data={
        "dbfiles": [
            "schema.yaml",
        ]
    },
    python_requires=">=3",
    platforms=["linux"]
)
