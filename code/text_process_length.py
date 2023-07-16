import argparse
import glob
import re
from misc import *
import re

# fix the length use splitByMaxLength function
# python text_process_length.py --input filename --ouput filename --minlength 1 --maxlength 128

# init the parser
parse = argparse.ArgumentParser(description='Preprocess the text data, cut long sentences into small sentences.')
parse.add_argument('--input', type=str, help='input file name')
parse.add_argument('--output', type=str, help='output file name')
parse.add_argument('--minlength', type=int, help='minimum length of the sentence', default=32)
parse.add_argument('--maxlength', type=int, help='maximum length of the sentence', default=1024)
args = parse.parse_args()

# variables
input_file = args.input
output_file = args.output
minlength = args.minlength
maxlength = args.maxlength

# read the file
with open(input_file, 'r') as f:
  lines = f.readlines()

for line in lines:
  line = line.strip()
  if line == "":
    continue

  # split the sentence
  sentences = splitByMaxLength(line, minlength, maxlength)
  for sentence in sentences:
    with open(output_file, 'a') as f:
      f.write(sentence + "\n")