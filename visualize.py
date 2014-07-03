#!/usr/bin/env python

import json
import math
import numpy
import os
import re
import sys

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('usage: %s [result dir] [output html]' % sys.argv[0])
        sys.exit()

    result = [[], [], [], []]
    for filename in os.listdir(sys.argv[1]):
        match = re.match('([0-9]+)_([0-9]+).result', filename)
        if not match:
            continue

        average, size = map(int, match.groups())
        name = 'Average: %d, Size: %d' % (average, size)

        matrix = numpy.loadtxt(os.path.join(sys.argv[1], filename), dtype = str)
        data = matrix[1:,1:].astype(int)
        result[0].append([numpy.mean(data[:,3]), numpy.mean(data[:,4]), len(data), name])
        result[1].append([numpy.median(data[:,3]), numpy.median(data[:,4]), len(data), name])
        result[2].append([numpy.amin(data[:,3]), numpy.amin(data[:,4]), len(data), name])
        result[3].append([numpy.amax(data[:,3]), numpy.amax(data[:,4]), len(data), name])
    
    path = os.path.join(os.path.dirname(__file__), 'html')
    with open(os.path.join(path, 'template.html')) as input:
        with open(sys.argv[2], 'w') as output:
            relpath = os.path.relpath(path, os.path.dirname(sys.argv[2]))

            html = input.read()
            format = [relpath] * 5 + map(json.dumps, result)
            output.write(html % tuple(format))
