ldtp library for Robot Framework
==================================================

.. image:: https://api.travis-ci.org/wywincl/LDTPLibrary.svg
    :target: https://travis-ci.org/wywincl/LDTPLibrary

.. image:: https://coveralls.io/repos/github/wywincl/LDTPLibrary/badge.svg?branch=master
    :target: https://coveralls.io/github/wywincl/LDTPLibrary?branch=master

.. image:: https://img.shields.io/pypi/v/robotframework-ldtplibrary.svg
    :target: https://pypi.python.org/pypi/robotframework-ldtplibrary

.. image:: https://img.shields.io/pypi/dm/robotframework-ldtplibrary.svg
    :target: https://pypi.python.org/pypi/robotframework-ldtplibrary

.. image:: https://img.shields.io/pypi/l/robotframework-ldtplibrary.svg
    :target: http://www.apache.org/licenses/LICENSE-2.0


Introduction
------------

LDTPLibrary is a linux desktop GUI application testing library for `Robot Framework`_
that leverages the `ldtp`_ libraries from the
LDTP project.

- More information about this library can be found on the `Wiki`_ and in the `Keyword Documentation`_.
- Installation information is found in the `INSTALL.rst`_ file.
- Developer information is found in `BUILD.rst`_ file.


Installation
------------

Using ``pip``
'''''''''''''

The recommended installation method is using
`pip <http://pip-installer.org>`_::

    pip install robotframework-ldtplibrary

The main benefit of using ``pip`` is that it automatically installs all
dependencies needed by the library. Other nice features are easy upgrading
and support for un-installation::

    pip install --upgrade robotframework-ldtplibrary
    pip uninstall robotframework-ldtplibrary

Notice that using ``--upgrade`` above updates both the library and all
its dependencies to the latest version. If you want, you can also install
a specific version or upgrade only the ldtp tool used by the library::

    pip install robotframework-ldtplibrary==10.1.0
    pip install --upgrade ldtp
    pip install ldtp==3.6.0

Proxy configuration
'''''''''''''''''''

If you are behind a proxy, you can use ``--proxy`` command line option
or set ``http_proxy`` and/or ``https_proxy`` environment variables to
configure ``pip`` to use it. If you are behind an authenticating NTLM proxy,
you may want to consider installing `CNTML <http://cntlm.sourceforge.net>`__
to handle communicating with it.

For more information about ``--proxy`` option and using pip with proxies
in general see:

- http://pip-installer.org/en/latest/usage.html
- http://stackoverflow.com/questions/9698557/how-to-use-pip-on-windows-behind-an-authenticating-proxy
- http://stackoverflow.com/questions/14149422/using-pip-behind-a-proxy

Manual installation
'''''''''''''''''''

If you do not have network connection or cannot make proxy to work, you need
to resort to manual installation. This requires installing both the library
and its dependencies yourself.

1) Make sure you have `Robot Framework installed
   <http://code.google.com/p/robotframework/wiki/Installation>`__.

2) Download source distributions (``*.tar.gz``) for the library and its
   dependencies:

   - https://pypi.python.org/pypi/robotframework-ldtplibrary
   - https://pypi.python.org/pypi/ldtp
   - https://pypi.python.org/pypi/decorator

3) Extract each source distribution to a temporary location.

4) Go each created directory from the command line and install each project
   using::

       python setup.py install

If you are on Windows, and there are Windows installers available for
certain projects, you can use them instead of source distributions.
Just download 32bit or 64bit installer depending on your system,
double-click it, and follow the instructions.

Directory Layout
----------------

demo/
    A simple demonstration

doc/
    Keyword documentation

src/
    Python source code

test/
    Unit test and acceptance test for LDTPLibrary


Usage
-----

To write tests with Robot Framework and LDTPLibrary,
LDTPLibrary must be imported into your Robot test suite.
See `Robot Framework User Guide`_ for more information.


.. _Robot Framework: http://robotframework.org
.. _ldtp: http://ldtp.freedesktop.org/wiki/
.. _Wiki: https://github.com/wywincl/LDTPLibrary/wiki
.. _Keyword Documentation: http://robotframework.org/LDTPLibrary/doc/LDTPLibrary.html
.. _INSTALL.rst: https://github.com/wywincl/LDTPLibrary/blob/master/INSTALL.rst
.. _BUILD.rst: https://github.com/wywincl/LDTPLibrary/blob/master/BUILD.rst
.. _Robot Framework User Guide: http://code.google.com/p/robotframework/wiki/UserGuide
.. _user group for Robot Framework: http://groups.google.com/group/robotframework-users
