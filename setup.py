#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    import ez_setup
    ez_setup.use_setuptools()
    from setuptools import setup

setup(
    name = "django-piston",
    version = "0.3.1",
    url = 'https://github.com/SheepDogInc/django-piston',
    download_url = 'https://github.com/SheepDogInc/django-piston',
    license = 'BSD',
    description = "Piston is a Django mini-framework creating APIs.",
    author = 'Jesper Noehr',
    author_email = 'jesper@noehr.org',
    packages = ['piston'],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    test_suite='piston.tests.runtests.runtests'
)
