# ----------------------------------------------------------------------------
# Copyright (c) 2016-2018, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from setuptools import setup, find_packages


setup(
    name="q2-sqrt",
    version='0.0.1.dev',
    packages=find_packages(),
    package_data={},
    author="All of us",
    author_email="ebolyen@gmail.com",
    description="Calculate square root and bray-curtis",
    license='BSD-3-Clause',
    url="https://qiime2.org",
    entry_points={
        'qiime2.plugins': ['q2-sqrt=q2_sqrt.plugin_setup:plugin']
    },
    zip_safe=False,
)
