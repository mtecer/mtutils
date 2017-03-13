#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Project: mtutils
File:    package.py
"""

from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import *

import jinja2
import os
import re
import shutil
import sys
import time
import yaml


def create_package(args):
    year, month, day, hour, minute = time.strftime("%Y,%m,%d,%H,%M").split(',')
    current_dir = os.getcwd()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    configfile = os.path.join(base_dir,'data/config.yaml')

    with open(configfile,'r') as yamlconfig:
        config = yaml.load(yamlconfig)

    package_dirs = config['package_dirs']
    package_files = config['package_files']

    package_name = args.create
    package_dirs.append(package_name)

    for dir in package_dirs:
        os.makedirs(os.path.join(package_name, dir), exist_ok=True)

    context = {
        'author': config['author'],
        'author_email': config['author_email'],
        'package_name': package_name,
        'package_url':  os.path.join(config['package_url'], package_name),
        'year': year,
    }

    print(base_dir)

    for file in package_files:
        if file['name'] == '__MODULE_FILE__.py':
            file['name'] = re.sub(r'__MODULE_FILE__', package_name,file['name'])

        if file['name'] == '__MODULE_RUNNER__.py':
            file['name'] = re.sub(r'__MODULE_RUNNER__', package_name + '-runner' ,file['name'])

        if file['path']:
            file['path'] = re.sub(r'__MODULE_DIR__', package_name,file['path'])
            file_path = os.path.join(package_name, file['path'],file['name'])
        else:
            file_path = os.path.join(package_name, file['name'])

        j2_env = jinja2.Environment(loader=jinja2.FileSystemLoader(base_dir))
        template = os.path.join('templates', file['template'])
        content = j2_env.get_template(template).render(context)

        with open(file_path, 'w+') as f:
            f.write(content + "\n")

    sys.exit()





    current_dir = os.getcwd()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # temp_dir = os.path.join(base_dir,'templates')
    # tgt_dir = os.path.join(base_dir,'base')



    j2_env = jinja2.Environment(loader=jinja2.FileSystemLoader(base_dir))
    result = j2_env.get_template('templates/runner.py.j2').render(context)

    # with open('files/test.txt','a+') as f:
    #     f.write(result + "\n")

    for file, file_info in package_files.items():
        for k, v in file_info.items():
            print(file, k, v)
        # for k, v in data:
        #     print(k,v)

    #
    # if not os.path.exists(tgt_dir):
    #     os.mkdir(tgt_dir)
    #
    # if not os.path.exists("/Users/mtecer/Py/mtutils/mtutils/base/testfile"):
    #     print("doesn't exists")








def delete_package(args):
    package_name = args.create
    package_dirs.append(package_name)

    if os.path.isdir(args.delete):
        confirm_package = False

        for subdirs in package_dirs:
            if os.path.isdir(os.path.join(args.delete,subdirs)):
                confirm_package = True
            else:
                print("Not a package")
                confirm_package = False
                break

        if confirm_package:
            shutil.rmtree(args.delete)
