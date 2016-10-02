#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2015-2016 Wang Yang
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""Setup script for Robot's LDTPLibrary distributions"""
try:
    from ez_setup import use_setuptools
    use_setuptools()
except ImportError:
    pass

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


import sys
from os.path import join, dirname
sys.path.append(join(dirname(__file__), 'src'))

fileToExec = join(dirname(__file__), 'src', 'LDTPLibrary', 'version.py')

#execfile(join(dirname(__file__), 'src', 'LDTPLibrary', 'version.py'))
#execfile(fileToExec) # python2

with open(fileToExec) as f: # python3
    code = compile(f.read(), fileToExec, 'exec')
    exec(code)

DESCRIPTION = """
LDTPLibrary is a linux desktop testing library for Robot Framework
that leverages the LDTP(Linux Desktop Test Project) libraries.
"""[1:-1]

setup(name='robotframework-ldtplibrary',
      version=VERSION,
      description='linux desktop testing library for Robot Framework',
      long_description=DESCRIPTION,
      author='John.Wang',
      author_email='<wywincl@gmail.com>',
      url='https://github.com/wywincl/LDTPLibrary',
      license='Apache License 2.0',
      keywords='robotframework testing test automation ldtp dogtail AT-SPI GUI',
      platforms='any',
      classifiers=[
                        "Development Status :: 5 - Production/Stable",
                        "License :: OSI Approved :: Apache Software License",
                        "Operating System :: OS Independent",
                        "Programming Language :: Python",
                        "Topic :: Software Development :: Testing"
                     ],
      install_requires=[
          'decorator >= 3.3.2',
          'robotframework >= 2.9.0',
          'docutils >= 0.8.1',
          # 'ldtp >= 3.5.0', need ldtp, but pip sources does not existed.
      ],
      py_modules=['ez_setup'],
      package_dir={'': 'src'},
      packages=['LDTPLibrary', 'LDTPLibrary.keywords',
                'LDTPLibrary.utils'],
      include_package_data=True,
      )
