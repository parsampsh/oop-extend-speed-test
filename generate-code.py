#!/usr/bin/env python3
import sys

langs_init = {
    'php': '<?php class c1 {}',
    'python': 'class c1: pass',
}
class_defs = {
    'php': lambda i: 'class c' + str(i) + ' extends c' + str(i-1) + ' {}',
    'python': lambda i: 'class c' + str(i) + '(c' + str(i-1) + '): pass',
}

# show the help
if '--help' in sys.argv:
    print('Usage: python generate-code.py <lang> <count>')
    print('Example: python generate-code.py php 50000')
    sys.exit()

# get the language name argument
try:
    selected_lang = sys.argv[1]
except:
    selected_lang = 'php'

# get the count argument
try:
    count = int(sys.argv[2])
except:
    count = 10000

# search for the language
try:
    init_part = langs_init[selected_lang]
    class_def = class_defs[selected_lang]
except:
    print('Language not found')
    sys.exit(1)

# generate the code
code = init_part + '\n'
for i in range(2, count):
    code += class_def(i) + '\n'

# return the generated code
print(code)
