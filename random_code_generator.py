#!/usr/bin/env python

from __future__ import print_function
import random
import string
from optparse import OptionParser


def generate_random_code(count, length, show_hyphen=False):
    alnum = string.ascii_letters + string.digits
    for i in range(count):
        serial = ''
        for x in range(length):
            serial += random.choice(alnum)
            if show_hyphen and (x + 1) % 4 == 0 and (x + 1) != length:
                serial += '-'
        yield serial


def usage():
    print('Usage: python random_code_generator.py '
          '--count {count} --length {length} [--hyphen]')


if __name__ == '__main__':
    import sys
    parser = OptionParser()
    parser.add_option('--count', dest='count', type='int')
    parser.add_option('--length', dest='length', type='int')
    parser.add_option('--hyphen', action='store_true',
                      dest='show_hyphen', default=False)
    (options, args) = parser.parse_args()

    count = options.count
    length = options.length
    show_hyphen = options.show_hyphen

    try:
        assert count
        assert length

        for line in generate_random_code(count, length, show_hyphen):
            print(line)
    except AssertionError:
        usage()
        sys.exit(1)

# vim: set fenc=utf8 expandtab sw=4 ts=4:
