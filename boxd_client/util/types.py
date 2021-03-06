#!/usr/bin/env python
# -*- coding: utf-8 -*-


text_types = (str, )
integer_types = (int, )


def is_bytes(value):
    return isinstance(value, bytes)


def is_str(value):
    return isinstance(value, text_types)


def is_list(value):
    return isinstance(value, list)


def is_number(value):
    return isinstance(value, integer_types) and not isinstance(value, bool)


def is_dict(value):
    return isinstance(value, dict)
