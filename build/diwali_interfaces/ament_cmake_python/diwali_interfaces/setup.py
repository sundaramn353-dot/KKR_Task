from setuptools import find_packages
from setuptools import setup

setup(
    name='diwali_interfaces',
    version='0.1.0',
    packages=find_packages(
        include=('diwali_interfaces', 'diwali_interfaces.*')),
)
