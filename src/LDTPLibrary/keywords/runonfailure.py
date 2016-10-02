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

from robot.libraries import BuiltIn
from .keywordgroup import KeywordGroup

BUILTIN = BuiltIn.BuiltIn()


class RunOnFailureKeywords(KeywordGroup):
    def __init__(self):
        self._run_on_failure_keyword = None
        self._run_on_failure_keyword_args = None
        self._running_on_failure_routine = False

    # Public

    def register_keyword_to_run_on_failure(self, keyword, *args):
        """
        设置出错时候，执行的关键字

        :参数 keyword: 执行关键字

        :返回值: 关键字文本
        """
        old_keyword = self._run_on_failure_keyword
        old_keyword_text = old_keyword if old_keyword is not None else "No keyword"

        new_keyword = keyword if keyword.strip().lower() != "nothing" else None
        new_keyword_text = new_keyword if new_keyword is not None else "No keyword"

        self._run_on_failure_keyword = new_keyword
        self._run_on_failure_keyword_args = args
        self._info('%s will be run on failure.' % new_keyword_text)

        return old_keyword_text

    # Private

    def _run_on_failure(self):
        if self._run_on_failure_keyword is None:
            return
        if self._running_on_failure_routine:
            return
        self._running_on_failure_routine = True
        try:
            BUILTIN.run_keyword(self._run_on_failure_keyword, *self._run_on_failure_keyword_args)
        except Exception as err:
            self._run_on_failure_error(err)
        finally:
            self._running_on_failure_routine = False

    def _run_on_failure_error(self, err):
        err = "Keyword '%s' could not be run on failure: %s" % (self._run_on_failure_keyword, err)
        if hasattr(self, '_warn'):
            self._warn(err)
            return
        raise Exception(err)
