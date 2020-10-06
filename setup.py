#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import setup
from dbfiles import __version__

setup(
    name="dbfiles",
    version=__version__,
    description="dbfiles - util for archive you sql files into makeself archive",
    license='MIT',
    author="Stepan Perlov",
    author_email="stepanperlov@gmail.com",
    install_requires=[
        "PyYAML",
        "jsonschema",
    ],
    packages=["dbfiles"],
    entry_points={
        "console_scripts": [
            "dbfiles = dbfiles.main:main",
        ]
    },
    package_data={
        "dbfiles": [
            "makeself/*",
            "protocol.yaml",
        ]
    },
    python_requires=">=3",
    platforms=["linux"]
)
