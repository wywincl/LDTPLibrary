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

import os
from robot.api import logger
from .keywordgroup import KeywordGroup
from robot.libraries.BuiltIn import BuiltIn

try:
    from robot.libraries.BuiltIn import RobotNotRunningError
except ImportError:
    RobotNotRunningError = AttributeError


class LoggingKeywords(KeywordGroup):
    # Private

    @staticmethod
    def _debug(message):
        logger.debug(message)

    @staticmethod
    def _get_log_dir():
        try:
            variables = BuiltIn().get_variables()
            logfile = variables['${LOG FILE}']
            if logfile != 'NONE':
                return os.path.dirname(logfile)
            return variables['${OUTPUTDIR}']
        except RobotNotRunningError:
            return os.getcwd()

    @staticmethod
    def _html(message):
        logger.info(message, True, False)

    @staticmethod
    def _info(message):
        logger.info(message)

    def _log(self, message, level='INFO'):
        level = level.upper()
        if level == 'INFO':
            self._info(message)
        elif level == 'DEBUG':
            self._debug(message)
        elif level == 'WARN':
            self._warn(message)
        elif level == 'HTML':
            self._html(message)

    def _log_list(self, items, what='item'):
        msg = ['Altogether %d %s%s.' % (len(items), what, ['s', ''][len(items) == 1])]
        for index, item in enumerate(items):
            msg.append('%d: %s' % (index + 1, item))
        self._info('\n'.join(msg))
        return items

    @staticmethod
    def _warn(message):
        logger.warn(message)
