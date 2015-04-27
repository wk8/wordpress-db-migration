#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse

from data_replacer import DataReplacer


def main():
    parser = argparse.ArgumentParser(
        description='Searches and replaces through a WP dump file to change the site\'s URL'
    )
    parser.add_argument('--from', dest='search', metavar='OLD_SITE_URL', help='The old URL', type=str, nargs=1, required=True)
    parser.add_argument('--to', dest='replace', metavar='NEW_SITE_URL', help='The new URL', type=str, nargs=1, required=True)
    parser.add_argument('--in', dest='input', metavar='IN_FILE', help='The input SQL dump file', type=str, nargs=1, required=True)
    parser.add_argument('--out', dest='output', metavar='OUT_FILE', help='The output SQL dump file', type=str, nargs=1, required=True)
    args = parser.parse_args()

    replacer = DataReplacer(args.search[0], args.replace[0])
    i = 0

    with open(args.input[0], 'r') as input_file:
        with open(args.output[0], 'w') as output_file:
            while True:
                line = input_file.readline()
                if not line:
                    break
                output_file.write(replacer.process(line))
                i += 1
                if (i % 1000 == 0):
                    print 'Processed %s lines...' % (i)

    print 'Done! Made %s replacements across %s lines' % (replacer.count, i)

main()
