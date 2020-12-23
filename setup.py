#!/usr/bin/env python

import sys
from setuptools import setup

if sys.version_info < (3, 6):
    raise NotImplementedError("Sorry, you need at least Python 3.6 to use nanoasgi.")

import nanoasgi

setup(name='NanoASGI',
      version=nanoasgi.__version__,
      description='Fast and simple ASGI-framework for small web-applications.',
      long_description=nanoasgi.__doc__,
      long_description_content_type="text/markdown",
      author=nanoasgi.__author__,
      author_email='kavindusanthusa@gmail.com',
      url='http://nanoasgi.github.io/',
      py_modules=['nanoasgi'],
      scripts=['nanoasgi.py'],
      license='MIT',
      platforms='any',
      classifiers=['Development Status :: 4 - Beta',
                   "Operating System :: OS Independent",
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries',
                   'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
                   'Topic :: Internet :: WWW/HTTP :: WSGI',
                   'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
                   'Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware',
                   'Topic :: Internet :: WWW/HTTP :: WSGI :: Server',
                   'Topic :: Software Development :: Libraries :: Application Frameworks',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.6',
                   'Programming Language :: Python :: 3.7',
                   'Programming Language :: Python :: 3.8',
                   ],
      )
