"""
Setup tool for package pylogger
"""
from setuptools import setup, find_packages

setup(
    name="pylogger",
    version="0.2",
    include_package_data=True,
    install_requires=[],
    dependency_links=[],
    test_suite='nose.collector',
    tests_require=['nose'],
    packages=['pylogger'],
)
