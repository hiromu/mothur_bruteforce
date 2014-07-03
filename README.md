# mother_parameter

calcurate and visualize the quality of sequence denosing against the combination of some parameters

## sample usage

    ./trim.py -f sample.fasta -q sample.qual -o sample.oligo -n 4 output
    ./visualize.py output result.html

## usage: trim.py

    Usage: trim.py [options] output_dir
    
    Options:
      -h, --help            show this help message and exit
      -f FASTA, --fasta=FASTA
                            name of fasta file
      -o OLIGOS, --oligos=OLIGOS
                            name of oligo file
      -q QFILE, --qfile=QFILE
                            name of qual file
      -v, --verbose         verbose
      -n PROCESSORS, --processors=PROCESSORS
                            numbers of processors for parallelizing [default: 1]
      --average-min=AVERAGE_MIN
                            minimum value of qwindowaverage [default: 25]
      --average-max=AVERAGE_MAX
                            maximum value of qwindowaverage [default: 75]
      --average-step=AVERAGE_STEP
                            step value of qwindowaverage [default: 5]
      --size-min=SIZE_MIN   minimum value of qwindowsize [default: 10]
      --size-max=SIZE_MAX   maximum value of qwindowsize [default: 100]
      --size-step=SIZE_STEP
                            step value of qwindowsize [default: 10]

## usage: visualize.py

    Usage: visualize.py result_dir output_html
