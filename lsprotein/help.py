#!/usr/bin/env python3

# help.py - Help source file of lsprotein
# Written by Ercan Ersoy (http://ercanersoy.net).

import lsprotein.version
import sys

def print_help_information():
    print('lsprotein ' + lsprotein.version.lsprotein_version)
    print()
    print('Protein lister on command line interface')
    print()
    print('Copyright (C) 2020 Ercan Ersoy (http://ercanersoy.net)')
    print()
    print('This software has been licensed by MIT License.')
    print()
    print('Usage:')
    print('  lsprotein protein_id [protein_id] [protein_id] ...')
    print('  lsprotein -h|--help')
    print()
    print('Command Line Parameters:')
    print('  -h, --help  Display help information and exit.')

    sys.exit(0)
