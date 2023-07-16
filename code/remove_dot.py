# randomly remove dot for half of the pairs in the listimport random
import random

# read the data
with open("../processed/04_test_rule_random_sample/preGOC_unique.txt", "r") as f, open("../processed/04_test_rule_random_sample/postGOC_unique.txt", "r") as g:
    pre_list = f.readlines()
    post_list = g.readlines()

# write to files
with open("../processed/04_test_rule_random_sample/preGOC_dot.txt", "w") as f, open("../processed/04_test_rule_random_sample/postGOC_dot.txt", "w") as g:
    for i, j in zip(pre_list, post_list):
        if i[-2] == "." and j[-2] == ".":
            if random.random() > 0.5:
                i = i[:-2] + "\n"
                j = j[:-2] + "\n"
        f.write(i)
        g.write(j)
