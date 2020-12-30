#!/usr/bin/env python3
import os
from pathlib import Path
import sys

__projectdir__ = Path(os.path.dirname(os.path.realpath(__file__)) + '/')

sys.path.append(str(__projectdir__ / Path('submodules/linux-keyshortcuts/')))
from shortcuts_func import parseshortcuts
shortcuts = parseshortcuts(__projectdir__ / Path('inputfile.txt'))

print('SHORTCUTS GENERAL LIST')
print(shortcuts)
print('')

sys.path.append(str(__projectdir__ / Path('submodules/linux-keyshortcuts/')))
from shortcuts_func import parsetoopenbox
openboxshortcuts = parsetoopenbox(__projectdir__ / Path('inputfile.txt'))

print('OPENBOX SHORTCUTS')
print(openboxshortcuts)
print('')
