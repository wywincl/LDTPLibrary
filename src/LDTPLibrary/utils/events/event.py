#!/usr/bin/env python
# -*- coding: utf-8 -*-
import abc


class Event(object):
    @abc.abstractmethod
    def trigger(self, *args, **kwargs):
        pass
