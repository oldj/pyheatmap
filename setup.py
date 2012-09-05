# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name="pyheatmap",
    version=__import__("pyheatmap.__init__").__version__,
    packages=["pyheatmap"],
    url="https://github.com/oldj/pyheatmap",
    license="LGPL",
    author="oldj",
    author_email="oldj.wu@gmail.com",
    description="Create heatmap by Python.",
    requires=["PIL"]
)
