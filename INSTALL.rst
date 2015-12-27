LDTPLibrary Installation
=============================


Preconditions
-------------

LDTPLibrary supports all Python and Jython interpreters supported by the
Robot Framework.

LDTPLibrary depends on a few other Python libraries, including
of course Robot Framework and ldtp. All dependencies are declared
in setup.py.


Installing from source
----------------------

The source code can be retrieved either as a source distribution or as a clone
of the main source repository. The installer requires Python version 2.6 or
newer. Install by running::

    python setup.py install

Or, if you'd like to automatically install dependencies, run::

    python setup.py develop

Note: In most linux systems, you need to have root privileges for installation.

Uninstallation is achieved by deleting the installation directory and its
contents from the file system. The default installation directory is
`[PythonLibraries]/site-packages/LDTPLibrary`.



Verifying Installation
----------------------

Once you have installed LDTPLibrary it is a good idea to verify the installation. To verify installation start python::

     C:\> python

and then at the Python prompt type::

	>> import LDTPLibrary
	>>

If the python command line interpreter returns with another prompt ('>>' as shown above) then your installation was successful.

Troubleshooting Installation
----------------------------

The most common issue with installing LDTPLibrary is missing dependencies. An error like::

    ImportError: No module named robot.variables

indicates that you are missing the Robot Framework package.  To correct this problem try typing at the prompt::

    easy_install robotframework

Similarly if you receive "No module named ..." error message then you have another missing dependency.  To correct, use easy_install to install the missing package.