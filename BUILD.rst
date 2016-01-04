LDTPLibrary Developer Information
======================================


Directory Layout
----------------

MANIFEST.in
    File that controls what gets included in a distribution

setup.py
    Setup script (uses setuptools)

demo/
    Demo gui app, acceptance tests, and scripts

doc/
    Scripts to build keyword and readme documentation

src/
    Library source code

test/
    Unit tests and acceptance tests for LDTPLibrary


Building a Distribution
-----------------------

To build a distribution, run::

	python build_dist.py <python 2.6 path> <python 2.7 path>

This script will:

- Generate source distribution packages in .tar.gz and .zip formats
- Generate Python eggs for Python 2.6 and 2.7
- Generate binary installers for Windows x86 and x64 (if run on Windows)
- Generate a demo distribution package in .zip format.
- Re-generate keyword documentation in doc folder

Note: The Windows installers will only be built if the script is run on
a Windows machine. If the rest of the distribution has been built on
a non-Windows machine and you want to build just the Windows installers,
use the --winonly flag::

    python build_dist.py --winonly <python 2.6 path> <python 2.7 path>



Building Keyword Documentation
------------------------------

The keyword documentation will get built automatically by build_dist.py,
but if you need to generate it apart from a distribution build, run::

    python doc/generate.py

