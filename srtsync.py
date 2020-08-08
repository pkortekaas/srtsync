#! /usr/bin/python3
import sys
import re
from datetime import datetime, timedelta

def main():
    if len(sys.argv) != 2:
        print("Specify offset in milliseconds")
        sys.exit(0)

    p = re.compile(
        r'^(?P<start>\d{2}:\d{2}:\d{2},\d{3})(?P<middle>[^0-9]*)' +
        r'(?P<end>\d{2}:\d{2}:\d{2},\d{3})(?P<fill>.*)$')

    o = int(sys.argv[1])
    offset = timedelta(milliseconds=o)
    parse = '%H:%M:%S,%f'

    for line in sys.stdin:
        m = p.match(line)
        if m:
            start = datetime.strptime(m.group('start'), parse) + offset
            end = datetime.strptime(m.group('end'), parse) + offset
            print("{}{}{}{}".format(
                start.strftime('%H:%M:%S,%f')[:-3], m.group('middle'),
                end.strftime('%H:%M:%S,%f')[:-3], m.group('fill')))
        else:
            print(line, end='')

if __name__ == '__main__':
    main()
