#!/usr/bin/env python
from os.path import dirname, join
from setuptools import setup, find_packages


setup(
    name='msi-backlight',
    version='2.1',
    description='Configuration tool for per-key RGB keyboards on MSI laptops.',
    long_description=open(
        join(dirname(__file__), 'README.md')).read(),
    author='Robin Lange',
    author_email='robin.langenc@gmail.com',
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'msi-backlight=msi_perkeyrgb.main:main',
        ],
    },
    package_data={'msi_perkeyrgb': ['protocol_data/presets/*.json']},
    keywords=['msi', 'rgb', 'keyboard', 'per-key'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
