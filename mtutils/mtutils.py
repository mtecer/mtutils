#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Project: mtutils
File:    mtutils.py
"""

from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import *

__version__ = "0.0.11"

import argparse

from mtutils.package import create_package, delete_package
from mtutils.file import search_files, search_content


def getargs():
    description = """CLI Utilities"""
    parser = argparse.ArgumentParser(description=description, formatter_class=argparse.RawTextHelpFormatter)
    parser.set_defaults(which='main')
    parser.add_argument('--version', action='version', version=__version__)

    subparsers = parser.add_subparsers(
        title='subcommands',
        description='valid subcommands',
        help='Additional help')

    package_parser = subparsers.add_parser('package',help='Python package utilities', description='Python package tools')
    package_parser.set_defaults(which='package')
    package_parser.add_argument('-c','--create', action='store', metavar='NAME', help='creates a template python package directory')
    package_parser.add_argument('-d','--delete', action='store', metavar='NAME', help='deletes a python package directory')

    file_parser = subparsers.add_parser('file', help='Python filesystem utilities', description='Filesystem tools')
    file_parser.set_defaults(which='file')
    file_parser.add_argument('-s','--search', action='store', metavar='NAME', help='searches for files matching a pattern')
    file_parser.add_argument('-c','--content', action='store', metavar='NAME', help='searches for text in files matching a pattern')

    return parser.parse_args()


def main():
    args = getargs()

    if args.which == 'main':
        print("You are in main menu")
    elif args.which == 'package':
        if args.create:
            create_package(args)
        elif args.delete:
            delete_package(args)
    elif args.which == 'file':
        if args.search:
            search_files()
        elif args.content:
            search_content()
