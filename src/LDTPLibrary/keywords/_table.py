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

import ldtp
from keywordgroup import KeywordGroup
from _exception import LdtpError


class TableKeywords(KeywordGroup):
    def __init__(self):
        self._client = ldtp

    def double_click_row_index(self, window_name, object_name, row_index, col_index=0):
        """
        Double click row matching given text

        @param window_name: Window name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type window_name: string
        @param object_name: Object name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type object_name: string
        @param row_index: Row index to click
        @type row_index: integer
        @param col_index: Column index to click
        @type col_index: integer

        @return: row index matching the text on success.
        @rtype: integer
        """
        self._info("double click row index, col index (%d,%d) of [%s, %s]" % (row_index, col_index,
                                                                              window_name, object_name))
        try:
            self._client.doubleclickrowindex(window_name, object_name, row_index, col_index)
        except LdtpError as e:
            raise LdtpError(e.message)
