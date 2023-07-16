import argparse
import glob
import re
from misc import *
from difflib import SequenceMatcher

# thanks for this post: https://linuxhint.com/add_command_line_arguments_to_a_python_script/#:~:text=To%20add%20arguments%20to%20Python,are%20of%20proper%20%E2%80%9Ctype%E2%80%9D.
parser = argparse.ArgumentParser(description='Data processing for row data including paired data, postGOC, preGOC.')
parser.add_argument("datatype", help="Data Type: paired, postGOC, preGOC")
args = parser.parse_args()

rowdataloc = "../rowdata/"+args.datatype+"/"
processedloc = "../processed/"+args.datatype+"/"

if args.datatype == "paired":
    paired = True
    pre_filenames = glob.glob(rowdataloc + "preGOC/*.txt")
    post_filenames = glob.glob(rowdataloc + "postGOC/*.txt")
else:
    paired = False
    pre_filenames = glob.glob(rowdataloc + "*.txt")
    post_filenames = glob.glob(rowdataloc + "*.txt")

if not paired:
    pre_files = ["_".join(i.split('/')[-1].split("_")[0:5]) for i in pre_filenames]
    post_files = ["_".join(i.split('/')[-1].split("_")[0:5]) for i in post_filenames]
else:
    pre_files = ["_".join(i.split('/')[-1].split("_")[0:5]) for i in pre_filenames]
    post_files = ["_".join(i.split('/')[-1].split("_")[0:5]) for i in post_filenames]
    print(pre_filenames, pre_files,post_filenames, post_files)
ids = list(set(pre_files) & set(post_files))
pre_id2filename = {i:j for i,j in zip(pre_files,pre_filenames)}
post_id2filename = {i:j for i,j in zip(post_files,post_filenames)}

pre_sentence, post_sentence = [], []
dic = {}

for m in ids:
    pre_list, post_list = file2listGOC(pre_id2filename, post_id2filename, m)
    
    presentence, postsentence = [], []
    score = []
    if paired:
        print("RUN Paired data")
        for i in pre_list:
            rowscore = []
            for j in post_list:
                dic[(i,j)] = similar(i,j)
                dic[(j,i)] = dic[(i,j)]
                rowscore.append(dic[(i,j)])
                if dic[(i,j)]>=0.9 and i != '. ':
                    pre, post = i, j
                    presentence.append(pre)
                    postsentence.append(post)
            score.append(rowscore)
        pre_sentence += presentence
        post_sentence += postsentence

    else:
        pre_sentence += pre_list
        post_sentence += post_list

training = [(i.strip(),j.strip()) if "˩˧" not in i else None for i,j in zip(pre_sentence,post_sentence)]
training = list(filter(None, training))
# save data
if args.datatype=="postGOC":
    g=open(processedloc+'postGOC.txt','w')

    for data in training:
        g.write(data[1]+'\n')

    g.close()
elif args.datatype =="preGOC":
    f=open(processedloc+'preGOC.txt','w')

    for data in training:
        f.write(data[0]+'\n')

    f.close()
elif args.datatype =="paired":
    f=open(processedloc+'preGOC.txt','w')
    g=open(processedloc+'postGOC.txt','w')

    for data in training:
        f.write(data[0]+'\n')
        g.write(data[1]+'\n')

    f.close()
    g.close()
