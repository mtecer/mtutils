#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""setup.py: setuptools control."""

import re

from setuptools import setup, find_packages


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('mtutils/mtutils.py').read(),
    re.M
    ).group(1)

requirements = [ i.strip() for i in open("requirements.txt").readlines() ]

with open("README.md", "rb") as f:
    long_description = f.read().decode("utf-8")


setup(
    name="mtutils",
    packages=find_packages(),
    install_requires = requirements,
    include_package_data = True,
    entry_points={
        "console_scripts": ['mtutils = mtutils.mtutils:main']
        },
    version=version,
    description="Python command line utilities.",
    long_description=long_description,
    author="Mehmet Tecer",
    author_email="mehmettecer@gmail.com",
    url="http://www.github.com/mtecer/mtutils",
    )
