# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in uber/__init__.py
from uber import __version__ as version

setup(
	name='uber',
	version=version,
	description='food dilevery',
	author='uber platform',
	author_email='uber@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
