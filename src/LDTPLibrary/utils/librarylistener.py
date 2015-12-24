#!/usr/bin/env python
# -*- coding: utf-8 -*-
import events as event


class LibraryListener(object):
    ROBOT_LISTENER_API_VERSION = 2

    def start_suite(self, name, attrs):
        event.dispatch('scope_start', attrs['longname'])

    def end_suite(self, name, attrs):
        event.dispatch('scope_end', attrs['longname'])

    def start_test(self, name, attrs):
        event.dispatch('scope_start', attrs['longname'])

    def end_test(self, name, attrs):
        event.dispatch('scope_end', attrs['longname'])
