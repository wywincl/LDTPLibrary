#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from .events import events as event
from .events import *


class LibraryListener(object):
    ROBOT_LISTENER_API_VERSION = 2

    def start_suite(self, name, attrs):
        dispatch('scope_start', attrs['longname'])

    def end_suite(self, name, attrs):
        dispatch('scope_end', attrs['longname'])

    def start_test(self, name, attrs):
        dispatch('scope_start', attrs['longname'])

    def end_test(self, name, attrs):
        dispatch('scope_end', attrs['longname'])
