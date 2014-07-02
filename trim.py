#!/usr/bin/env python

import optparse
import os
import shutil
import subprocess

def test(options, average, size, output_dir):
    if options.verbose:
        print('Trying with qwindowaverage = %d, qwindowsize = %d' % (average, size))

    command = '#trim.seqs(fasta=%s,oligos=%s,qfile=%s,qwindowaverage=%d,qwindowsize=%d,processors=%d)' % (options.fasta, options.oligos, options.qfile, average, size, options.processors)
    process = subprocess.Popen(['mothur', command], stdout = subprocess.PIPE)
    status = process.wait()
    if status != 0:
        return
    
    output = process.stdout.readlines()
    fasta = output[output.index('Output File Names: \n') + 1].strip()

    command = '#summary.seqs(fasta=%s)' % fasta
    process = subprocess.Popen(['mothur', command], stdout = subprocess.PIPE)
    status = process.wait()
    if status != 0:
        return

    output = process.stdout.readlines()
    result = output[output.index('Output File Names: \n') + 1].strip()

    shutil.copyfile(result, os.path.join(output_dir, '%d_%d.result' % (average, size)))

if __name__ == '__main__':
    parser = optparse.OptionParser(usage = 'usage: %prog [options] output_dir')

    parser.add_option('-f', '--fasta', help = 'name of fasta file')
    parser.add_option('-o', '--oligos', help = 'name of oligo file')
    parser.add_option('-q', '--qfile', help = 'name of qual file')

    parser.add_option('-v', '--verbose', help = 'verbose', action = 'store_true')
    parser.add_option('-n', '--processors', help = 'numbers of processors for parallelizing [default: %default]', type = 'int', default = 1)

    parser.add_option('--average-min', help = 'minimum value of qwindowaverage [default: %default]', default = 25)
    parser.add_option('--average-max', help = 'maximum value of qwindowaverage [default: %default]', default = 75)
    parser.add_option('--average-step', help = 'step value of qwindowaverage [default: %default]', default = 5)

    parser.add_option('--size-min', help = 'minimum value of qwindowsize [default: %default]', default = 10)
    parser.add_option('--size-max', help = 'maximum value of qwindowsize [default: %default]', default = 100)
    parser.add_option('--size-step', help = 'step value of qwindowsize [default: %default]', default = 10)

    options, args = parser.parse_args()
    if not options.fasta:
        parser.error('fasta file must be specified')
    if not options.oligos:
        parser.error('oligo file must be specified')
    if not options.qfile:
        parser.error('qual file must be specified')
    if len(args) < 1:
        parser.error('output_dir is required')

    if not os.path.exists(args[0]):
        os.mkdir(args[0])
    elif os.path.isfile(args[0]):
        parser.error('%s already exists' % args[0])

    for average in xrange(options.average_min, options.average_max + 1, options.average_step):
        for size in xrange(options.size_min, options.size_max + 1, options.size_step):
            test(options, average, size, args[0])
