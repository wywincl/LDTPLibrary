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

import sys
import inspect

try:
    from decorator import decorator
except SyntaxError:  # decorator module requires Python/Jython 2.4+
    decorator = None
if sys.platform == 'cli':
    decorator = None  # decorator module doesn't work with IronPython 2.6


def _run_on_failure_decorator(method, *args, **kwargs):
    self = args[0]
    already_in_keyword = getattr(self, "_already_in_keyword",
                                 False)
    # If False, we are in the outermost keyword (or in `run_keyword`,
    # if it's a dynamic library)
    self._already_in_keyword = True  # Set a flag on the instance so that as we call keywords inside this call and
    #  this gets run again, we know we're at least one level in.
    try:
        return method(*args, **kwargs)
    except Exception as err:
        if hasattr(self, '_run_on_failure') and not self._has_run_on_failure:
            # If we're in an inner keyword, track the fact that we've already run on failure once
            self._has_run_on_failure = True
            self._run_on_failure()
        raise
    finally:
        if not already_in_keyword:
            # If we are in the outer call, reset the flags.
            self._already_in_keyword = False
            self._has_run_on_failure = False


class KeywordGroupMetaClass(type):
    def __new__(mcs, cls_name, bases, dict_i):
        if decorator:
            for name, method in dict_i.items():
                if not name.startswith('_') and inspect.isroutine(method):
                    dict_i[name] = decorator(_run_on_failure_decorator, method)
        return type.__new__(mcs, cls_name, bases, dict_i)


class KeywordGroup(object):
    __metaclass__ = KeywordGroupMetaClass
