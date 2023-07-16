# make unique pairs from two files
# write to two files
with open("../processed/04_test_rule_random_sample/preGOC.txt", "r") as f, open("../processed/04_test_rule_random_sample/postGOC.txt", "r") as g:
    pre_list = f.readlines()
    post_list = g.readlines()

# set of tuples
pairs = set()
for i, j in zip(pre_list, post_list):
    pairs.add((i,j))

# write to files
with open("../processed/04_test_rule_random_sample/preGOC_unique.txt", "w") as f, open("../processed/04_test_rule_random_sample/postGOC_unique.txt", "w") as g:
    for i, j in pairs:
        f.write(i)
        g.write(j)