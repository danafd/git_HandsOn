#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")


if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()
#tells you whether the sequence you input is an RNA, DNA, or neither. 
args.seq = args.seq.upper()
if re.search('^[ACGTU]+$', args.seq):
    if re.search('T', args.seq) and re.search('U', args.seq): #This line checks whether the sequence contains both a T and U
        print('The sequence contains T and U')
    elif re.search('T', args.seq):
        print ('The sequence is DNA')
    elif re.search('U', args.seq):
        print ('The sequence is RNA')
    else:
        print ('The sequence can be DNA or RNA')
else:
    print ('The sequence is neither DNA nor RNA')

#searches for a motif in your sequence
if args.motif:
  args.motif = args.motif.upper()
  print(f'Motif search enabled: I am looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
  if re.search(args.motif, args.seq):
    print("FOUND IT!")
  else:
    print("COULD NOT FIND IT!")
