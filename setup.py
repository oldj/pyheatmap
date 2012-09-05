# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name="pyheatmap",
    version="0.1.3",
    packages=["pyheatmap", "pyheatmap.inc"],
    url="https://github.com/oldj/pyheatmap",
    license="LGPL",
    author="oldj",
    author_email="oldj.wu@gmail.com",
    description="Create heatmap by Python.",
    requires=["PIL"]
)
