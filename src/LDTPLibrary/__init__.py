#!/usr/bin/env python
# coding=utf-8
"""
Robot Framework LDTP Library

LDTPLibrary is a gui application testing library for Robot Framework.

It uses the LDTP (Linux Desktop Test Project) libraries internally to control a gui application.
See http://ldtp.freedesktop.org/wiki/ for more information on LDTP.

@author: Wang Yang <wywincl@gmail.com>
@copyright: Copyright (c) 2015-2016 Wang Yang
@license: GPLv3

See 'LICENSE' in the source distribution for more information.
"""

from .version import VERSION
from .keywords import *
from .utils import LibraryListener

__version__ = VERSION


class LDTPLibrary(LoggingKeywords,
                  RunOnFailureKeywords,
                  LDTPKeywords,
                  ScreenshotKeywords,
                  TableKeywords):
    """
    LDTPLibrary is a gui application testing library for Robot Framework.

    It uses the LDTP (Linux Desktop Test Project) libraries internally to control a gui application.
    See http://ldtp.freedesktop.org/wiki/ for more information on LDTP.

    Author: John.Wang <wywincl@gmail.com>

    Examples:

    |  *Settings*  |  *Value*  |
    |   Library    | LDTPLibrary |

    |  *Variables* |  *Value*  |
    |  ${APP_NAME} |  gnome-calculator |
    |  ${FRM_NAME} |  frmCalculator |

    |  *Test Cases*  |  *Action*  |  *Argument*  |  *Arguments*  |
    |  Example_Test  | Launch App | ${APP_NAME}  |               |
    |                | Click      | ${FRM_NAME}  |     btn1      |

    """

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = VERSION

    def __init__(self,
                 run_on_failure='Nothing',
                 screenshot_root_directory=None,
                 *args):
        """
        LDTPLibrary can be imported with optional arguments.

        :param [run_on_failure]:  specifies the name of a keyword (from any available
        libraries) to execute when a LDTPLibrary keyword fails. By default 'Nothing' will be used.
        "Nothing" will disable this feature altogether. See `Register Keywords To Run On Failure` keyword
        for more information about this functionality.

        Examples:
        | Library `|` LDTPLibrary  `|` run_on_failure = Log Source | # run `Log Source` on failure |
        | Library `|` LDTPLibrary  `|` run_on_failure = Capture Screenshot | # run `Capture Screenshot` on failure |
        | Library `|` LDTPLibrary  `|` run_on_failure = Capture Screenshot `|` out_file=/tmp/shot.png | # run `Capture Screenshot` on failure |
        | Library `|` LDTPLibrary  `|` run_on_failure = Nothing  | # does nothing on failure |
        | Library `|` LDTPLibrary  `|` run_on_failure = Capture Windows Screenshot `|` screenshot_root_directory=/tmp/ | # run `Capture Windows Screenshot ` on failure |

        """
        for base in LDTPLibrary.__bases__:
            base.__init__(self)
        self.screenshot_root_directory = screenshot_root_directory
        self.register_keyword_to_run_on_failure(run_on_failure, *args)
        self.ROBOT_LIBRARY_LISTENER = LibraryListener()
