#!/usr/bin/env python3

# help.py - Help source file of lsprotein
# Written by Ercan Ersoy (http://ercanersoy.net).

import lsprotein.version
import sys

def print_help_information():
    print('lsprotein ' + lsprotein.version.lsprotein_version)
    print('Protein lister on command line interface')
    print('Copyright (C) 2020 Ercan Ersoy (http://ercanersoy.net)')
    print('This software has been licensed by MIT License.')
    print()
    print('Usage:')
    print('  lsprotein protein_id [protein_id] [protein_id] ...')
    print('  lsprotein -h')
    print()
    print('Command Line Parameters:')
    print('  -h: Display help and exit.')

    sys.exit(0)
