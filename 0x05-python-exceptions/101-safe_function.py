#!/usr/bin/python3
from _future__ import print_function
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
