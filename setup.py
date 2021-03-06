# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from ads import __version__

REQUIREMENTS = [
    'Django>=1.8',
    'django-appconf>=1.0.2',
    'django-sekizai>=0.9.0'
]

CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
]

setup(
    name='django-ads',
    version=__version__,
    description='Ads Management System for Django Framework',
    author='Razi Alsayyed',
    author_email='razi.sayed@gmail.com',
    url='https://github.com/razisayyed/django-ads',
    packages=find_packages(),
    license='LICENSE',
    platforms=['OS Independent'],
    install_requires=REQUIREMENTS,
    classifiers=CLASSIFIERS,
    include_package_data=True,
    zip_safe=False
)
