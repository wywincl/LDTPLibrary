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
from .keywordgroup import KeywordGroup
from ._exception import LdtpError
from ldtp.client_exception import LdtpExecutionError


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

    def select_row_partial_match(self, window_name, object_name, row_text):
        """
        Select row partial match

        @param window_name: Window name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type window_name: string
        @param object_name: Object name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type object_name: string
        @param row_text: Row text to select
        @type row_text: string

        @return: 1 on success.
        @rtype: integer
        """
        try:
            self._info("select row partial match (%s, %s, %s) " % (window_name, object_name, row_text))
            return ldtp.selectrowpartialmatch(window_name, object_name, row_text)
        except LdtpExecutionError as e:
            raise LdtpExecutionError(e.message)

    def multi_select(self, window_name, object_name, row_text_list,
                     partial_match=False):
        """
        Select multiple row

        @param window_name: Window name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type window_name: string
        @param object_name: Object name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type object_name: string
        @param row_text_list: Row list with matching text to select
        @type row_text_list: string
        @param partial_match:

        @return: 1 on success.
        @rtype: integer
        """
        try:
            self._info("multi select  (%s, %s, %s) " % (window_name, object_name, row_text_list))
            return ldtp.multiselect(window_name, object_name, row_text_list)
        except LdtpExecutionError as e:
            raise LdtpExecutionError(e.message)

    def multi_remove(self, window_name, object_name, row_text_list,
                     partial_match=False):
        """
        Remove multiple row

        @param window_name: Window name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type window_name: string
        @param object_name: Object name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type object_name: string
        @param row_text_list: Row list with matching text to select
        @type row_text_list: string
        Args:
            partial_match:

        @return: 1 on success.
        @rtype: integer

        """
        try:
            self._info("multi remove  (%s, %s, %s) " % (window_name, object_name, row_text_list))
            return ldtp.multiremove(window_name, object_name, row_text_list)
        except LdtpExecutionError as e:
            raise LdtpExecutionError(e.message)

    def select_row_index(self, window_name, object_name, row_index):
        """
        Select row index

        @param window_name: Window name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type window_name: string
        @param object_name: Object name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type object_name: string
        @param row_index: Row index to select
        @type row_index: integer

        @return: 1 on success.
        @rtype: integer
        """
        try:
            self._info("select row index (%s, %s, %d)" % (window_name, object_name, row_index))
            return ldtp.selectrowindex(window_name, object_name, row_index)
        except LdtpExecutionError as e:
            raise LdtpExecutionError(e.message)

    def select_last_row(self, window_name, object_name):
        """
        Select last row

        @param window_name: Window name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type window_name: string
        @param object_name: Object name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type object_name: string

        @return: 1 on success.
        @rtype: integer
        """
        try:
            self._info("select last row of (%s, %s)" % (window_name, object_name))
            return ldtp.selectlastrow(window_name, object_name)
        except LdtpExecutionError as e:
            raise LdtpExecutionError(e.message)

    def set_cell_value(self, window_name, object_name, row_index,
                       column=0, data=None):
        """
        Set cell value

        @param window_name: Window name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type window_name: string
        @param object_name: Object name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type object_name: string
        @param row_index: Row index to get
        @type row_index: integer
        @param column: Column index to get, default value 0
        @type column: integer
        @param data: data, default value None
                None, used for toggle button
        @type data: string

        @return: 1 on success.
        @rtype: integer
        """
        try:
            self._info("set cell value (%s, %s, data=%s)" % (window_name, object_name, data))
            return ldtp.setcellvalue(window_name, object_name, row_index, column, data)
        except LdtpExecutionError as e:
            raise LdtpExecutionError(e.message)

    def get_cell_value(self, window_name, object_name, row_index, column=0):
        """
        Get cell value

        @param window_name: Window name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type window_name: string
        @param object_name: Object name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type object_name: string
        @param row_index: Row index to get
        @type row_index: integer
        @param column: Column index to get, default value 0
        @type column: integer

        @return: cell value on success.
        @rtype: string
        """
        try:
            self._info("get cell value (%s, %s, %d)" % (window_name, object_name, row_index))
            return ldtp.getcellvalue(window_name, object_name, row_index, column)
        except LdtpExecutionError as e:
            raise LdtpExecutionError(e.message)

    def get_cell_size(self, window_name, object_name, row_index, column=0):
        """
        Get cell size

        @param window_name: Window name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type window_name: string
        @param object_name: Object name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type object_name: string
        @param row_index: Row index to get
        @type row_index: integer
        @param column: Column index to get, default value 0
        @type column: integer

        @return: x, y, width, height on success.
        @rtype: list
        """
        try:
            self._info("get cell size (%s, %s, %d)" % (window_name, object_name, row_index))
            return ldtp.getcellsize(window_name, object_name, row_index, column)
        except LdtpExecutionError as e:
            raise LdtpExecutionError(e.message)

    def right_click(self, window_name, object_name, row_text):
        """
        Right click on table cell

        @param window_name: Window name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type window_name: string
        @param object_name: Object name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type object_name: string
        @param row_text: Row text to click
        @type row_text: string

        @return: 1 on success.
        @rtype: integer
        """
        try:
            self._info("right click row object (%s, %s, %s)" % (window_name, object_name, row_text))
            return ldtp.rightclick(window_name, object_name, row_text)
        except LdtpExecutionError as e:
            raise LdtpExecutionError(e.message)

    def check_row(self, window_name, object_name, row_index, column=0):
        """
        Check row

        @param window_name: Window name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type window_name: string
        @param object_name: Object name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type object_name: string
        @param row_index: Row index to get
        @type row_index: integer
        @param column: Column index to get, default value 0
        @type column: integer

        @return: cell value on success.
        @rtype: string
        """
        try:
            self._info("check row at (%s, %s, %d)" % (window_name, object_name, row_index))
            return ldtp.checkrow(window_name, object_name, row_index, column)
        except LdtpExecutionError as e:
            raise LdtpExecutionError(e.message)

    def expand_table_cell(self, window_name, object_name, row_index, column=0):
        """
        Expand or contract table cell

        @param window_name: Window name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type window_name: string
        @param object_name: Object name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type object_name: string
        @param row_index: Row index to get
        @type row_index: integer
        @param column: Column index to get, default value 0
        @type column: integer

        @return: cell value on success.
        @rtype: string
        """
        try:
            self._info("expend table cell at (%s, %s, %d)" % (window_name, object_name, row_index))
            return ldtp.expendtablecell(window_name, object_name, row_index, column)
        except LdtpExecutionError as e:
            raise LdtpExecutionError(e.message)

    def uncheck_row(self, window_name, object_name, row_index, column=0):
        """
        Check row

        @param window_name: Window name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type window_name: string
        @param object_name: Object name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type object_name: string
        @param row_index: Row index to get
        @type row_index: integer
        @param column: Column index to get, default value 0
        @type column: integer

        @return: 1 on success.
        @rtype: integer
        """
        try:
            self._info("uncheck row at (%s, %s, %d)" % (window_name, object_name, row_index))
            return ldtp.uncheckrow(window_name, object_name, row_index, column)
        except LdtpExecutionError as e:
            raise LdtpExecutionError(e.message)

    def get_table_row_index(self, window_name, object_name, row_text):
        """
        Get table row index matching given text

        @param window_name: Window name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type window_name: string
        @param object_name: Object name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type object_name: string
        @param row_text: Row text to select
        @type row_text: string

        @return: row index matching the text on success.
        @rtype: integer
        """
        try:
            self._info("get table row with index (%s, %s, %s)" % (window_name, object_name, row_text))
            return ldtp.gettablerowindex(window_name, object_name, row_text)
        except LdtpExecutionError as e:
            raise LdtpExecutionError(e.message)

    def single_click_row(self, window_name, object_name, row_text):
        """
        Single click row matching given text

        @param window_name: Window name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type window_name: string
        @param object_name: Object name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type object_name: string
        @param row_text: Row text to select
        @type row_text: string

        @return: row index matching the text on success.
        @rtype: integer
        """
        try:
            self._info("single click row (%s, %s, %s)" % (window_name, object_name, row_text))
            return ldtp.singleclickrow(window_name, object_name, row_text)
        except LdtpExecutionError as e:
            raise LdtpExecutionError(e.message)

    def double_click_row(self, window_name, table_name, row_text):
        """
        Double click row matching given text

        :param window_name:

        :param table_name:

        :param row_text:

        :return:
        """
        try:
            self._info("double click row matching given text")
            return ldtp.doubleclickrow(window_name, table_name, row_text)
        except LdtpExecutionError:
            raise LdtpExecutionError("Double click row failed")

    def verify_table_cell(self, window_name, object_name, row_index,
                          column_index, row_text):
        """
        Verify table cell value with given text

        @param window_name: Window name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type window_name: string
        @param object_name: Object name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type object_name: string
        @param row_index: Row index to get
        @type row_index: integer
        @param column_index: Column index to get, default value 0
        @type column_index: integer
        @param row_text: Row text to match
        @type row_text: string

        @return: 1 on success 0 on failure.
        @rtype: integer
        """
        try:
            self._info("verify table cell text ")
            return ldtp.verifytablecell(window_name, object_name, row_index, column_index, row_text)
        except LdtpExecutionError as e:
            raise LdtpExecutionError(e.message)

    def does_row_exist(self, window_name, object_name, row_text,
                       partial_match=False):
        """
        Verify table cell value with given text

        @param window_name: Window name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type window_name: string
        @param object_name: Object name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type object_name: string
        @param row_text: Row text to match
        @type row_text: string
        @param partial_match: Find partial match strings
        @type partial_match:boolean

        @return: 1 on success 0 on failure.
        @rtype: integer
        """
        try:
            self._info("Does row exist (%s, %s, %s)" % (window_name, object_name, row_text))
            return ldtp.doesrowexist(window_name, object_name, row_text, partial_match)
        except LdtpExecutionError as e:
            raise LdtpExecutionError(e.message)

    def verify_partial_table_cell(self, window_name, object_name, row_index,
                                  column_index, row_text):
        """
        Verify partial table cell value

        @param window_name: Window name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type window_name: string
        @param object_name: Object name to type in, either full name,
        LDTP's name convention, or a Unix glob.
        @type object_name: string
        @param row_index: Row index to get
        @type row_index: integer
        @param column_index: Column index to get, default value 0
        @type column_index: integer
        @param row_text: Row text to match
        @type row_text: string

        @return: 1 on success 0 on failure.
        @rtype: integer
        """
        try:
            self._info("verify partial table cell ...")
            return ldtp.verifypartialtablecell(window_name, object_name, row_index, column_index, row_text)
        except LdtpExecutionError as e:
            raise LdtpExecutionError(e.message)
