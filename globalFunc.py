#!/usr/bin/python3
# -*- encoding: utf8 -*-

'''
Defines the global functions used in MI system
'''

def sign(arg):
    'Gets the sign of the expression FLAG: NON-EXPR-COMPATIBLE'
    if not hasattr(arg, '__sign__'): raise TypeError
    return arg.__sign__()

# the following lines simply serve for the ease of typing, and can/should be ignored.
alternative = 0; del alternative
support = 0; del support
