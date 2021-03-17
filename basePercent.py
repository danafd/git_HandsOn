#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-b", "--base", type = str, required = False, help = "base")


if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)


args = parser.parse_args()


dict={"A":0, "C":0, "T":0, "G":0, "U":0}
for i, args.base in enumerate(args.seq):
  dict[args.base]+=1

if args.base:
  print(dict[args.base]/len(args.seq)*100)
