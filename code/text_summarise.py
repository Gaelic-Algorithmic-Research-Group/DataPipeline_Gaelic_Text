import argparse
import glob
import re
from misc import *
import re

# summarize the given text files
# python text_summarise.py --input filename1 filename2 filename3 ... filenameN

# init the parser
parse = argparse.ArgumentParser(description='Preprocess the text data, cut long sentences into small sentences.')
parse.add_argument('--input', type=str, nargs='+', help='input file name')
args = parse.parse_args()

# variables
input_files = args.input

# read the file
for input_file in input_files:
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    
    # count the number of sentences
    total = 0
    for line in lines:
        line = line.strip()
        if line == "":
            continue
        total += 1
    
    # count the number of words
    words = 0
    for line in lines:
        line = line.strip()
        if line == "":
            continue
        words += len(line.split(" "))

    # count duplicate sentence in lines
    duplictes = len(lines) - len(set(lines))

    # print the result
    print("File: %s" % input_file)
    print("Total sentences: %d" % total)
    print("Total words: %d" % words)
    print("Average words per sentence: %f" % (words/total))
    print("Max words per sentence: %d" % max([len(line.split(" ")) for line in lines]))
    print("Min words per sentence: %d" % min([len(line.split(" ")) for line in lines]))
    print("Max character length per sentence: %d" % max([len(line) for line in lines]))
    print("Min character length per sentence: %d" % min([len(line) for line in lines]))
    print("Number of Duplicates: %d" % duplictes)

    # get the unique characters in the file
    fh = open(input_file,'r').read()
    unique_chars = set(fh)
    unique_chars_string = "".join(unique_chars)
    print("Unique characters: %s" % unique_chars_string)