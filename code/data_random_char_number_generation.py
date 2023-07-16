# Generate some random character to help Transformer learn how to keep things

# same cases: paired 213,022 words
# - ` `
# - `()`
# - `1923`
# - `0.2344`
# - English
# - English with number would be good?
# - [] {} "" <> ’‘”“”
# ！@#￥%……&*（）——+《》“”：；「」【】|~·`~!@#$%^&*()_+=-=-£
# 

import random
from random import seed
import string
import numpy as np

np.random.seed(0)
seed(1)

def generator(type="char"):
    '''
    type: char, number, English, mixture, Gaelic, quate
    '''
    if type == "char":
        charlist = set(list("！@#￥%……&*（）——+《》“”：；「」【】|~·`~!#$%^&*()+=-=-£ ©"))
    with open("processed/paired/symbol.txt", "w") as f:
        for i in range(0,200):
            f.write("".join(random.choices(list(charlist),k = int(np.random.normal(100,10))))+"\n")
# # seed random number generator
# seed(1)
# generate random numbers between 0-1
    with open("processed/paired/symbol.txt", "a") as f:
        for i in range(0,200):
            for _ in range(15):
                value = random.random() + np.random.normal(0,100)
                f.write(format(value,'.2f'))
                f.write(" ")
            f.write("\n")
    with open("processed/paired/symbol.txt", "a") as f:
        for i in range(0,20):
            for _ in range(int(np.random.normal(100,30))):
                f.write(" ")
            f.write("\n")
generator()