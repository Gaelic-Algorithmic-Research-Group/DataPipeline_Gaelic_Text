
import random
# write a function that randomly select subsequence pairs from a list of pairs
# for example: we have pairs ("hello, world thiss Junfan", "hello, world this is Junfan")
# we want to randomly select a subsequence pair ("world thiss Junfan", "world this is Junfan"), ("thiss Junfan", "this is Junfan") and so on
# the length of the subsequence is randomly selected from 1 to the length of the original sequence
# set ramdom seed
random.seed(0)


# note that sometimes the words in the subsequence are not aligned, for example, ("Cha robh esan a' dolna bu mhiosa; cha robhsìon na b' fheàrr. ", "Cha robh esana' dol na bu mhiosa; cha robh sìon na b' fheàrr.")
# in this case, we need to align the subsequence pair
# for example, ("Cha robh esan a' dolna bu mhiosa", "Cha robh esana' dol na bu mhiosa") -> ("Cha robh esan a' dolna bu mhiosa", "Cha robh esana' dol na bu mhiosa")
# then we can randomly select a subsequence pair ("Cha robh esan a' dolna bu mhiosa", "Cha robh esana' dol na bu mhiosa") -> ("Cha robh esan a' dolna bu mhiosa", "Cha robh esana' dol na bu mhiosa")

def randomSubsequencePairAligned(pre, post):
    '''
    Randomly select a subsequence pair from a list of pairs.
    '''
    # # randomly select a pair
    # pair_index = random.randint(0, len(pre_list)-1)
    # pre = pre_list[pair_index]
    # post = post_list[pair_index]
    
    # randomly select a subsequence
    subsequence_length = random.randint(1, len(pre.split(" ")))
    subsequence = " ".join(pre.split(" ")[-subsequence_length:])
    
    # find the subsequence in the post
    post_subsequence = post.split(" ")[-subsequence_length:]
    post_subsequence = " ".join(post_subsequence)
    

    # align the subsequence
    aligned_subsequence, aligned_post_subsequence = align(subsequence, post_subsequence)
    # print("aligned subsequence: ", aligned_subsequence)
    # print("aligned post_subsequence: ", aligned_post_subsequence)
    if aligned_subsequence == 0 or aligned_post_subsequence == 0:
        return pre, post
    return aligned_subsequence, aligned_post_subsequence


def align(subsequence, post_subsequence):
    '''
    Align the subsequence pair.
    '''
    # split the subsequence into words
    subsequence_words = subsequence.split(" ")
    post_subsequence_words = post_subsequence.split(" ")
    
    # find the index of the first word in the subsequence
    index = -1
    for i in range(len(post_subsequence_words)):
        if post_subsequence_words[i] == subsequence_words[0]:
            index = i
            break
    if index == -1:
        return 0,0
    # align the subsequence
    aligned_subsequence = " ".join(subsequence_words[0:index+len(subsequence_words)])
    aligned_post_subsequence = " ".join(post_subsequence_words[index:])
    
    return aligned_subsequence, aligned_post_subsequence
    

# write a function that remove the unsimilar sequence pairs
# for example: we have pairs ("okay, world thiss Junfan", "hello, world this is Junfan")
# we want to remove this pair because the subsequence "okay" is not similar to "hello"

# load txt from ../processed/01_test_paired_only/postGOC_clean.txt and ../processed/01_test_paired_only/preGOC_clean.txt to test the randomSubsequencePair function

# generate N list of random pairs with min length == 32, 
def generateRandomPairs(pre_list, post_list, min_length=32, num_pairs=10):
    '''
    Generate N list of random pairs with min length == 32.
    '''
    # generate N list of random pairs
    random_pairs = set()
    for i in range(num_pairs):
        # randomly select a pair
        pair_index = random.randint(0, len(pre_list)-1)
        pre = pre_list[pair_index]
        post = post_list[pair_index]
        # print("original subsequence: ", pre)
        # print("original post_subsequence: ", post)
        pre, post = randomSubsequencePairAligned(pre, post)
        reversedpre = pre[::-1]
        reversedpost = post[::-1]
        reversedpre, reversedpost = randomSubsequencePairAligned(reversedpre, reversedpost)
        pre = reversedpre[::-1]
        post = reversedpost[::-1]
        # print("final pre:",pre)
        # print("final post:", post)
        
        if len(pre) > min_length and len(post) > min_length:
            random_pairs.add((pre, post))
        else:
            idx = random.randint(0,len(pre_list)-1)
            random_pairs.add((pre_list[idx], pre_list[idx]))
    return random_pairs

with open("../processed/01_test_paired_only/postGOC_clean.txt", "r") as f:
    post_list = f.readlines()

with open("../processed/01_test_paired_only/preGOC_clean.txt", "r") as f:
    pre_list = f.readlines()

random_pairs = generateRandomPairs(pre_list, post_list, num_pairs=5000000)

# write to two files
with open("../processed/04_test_rule_random_sample/preGOC.txt", "w") as f, open("../processed/04_test_rule_random_sample/postGOC.txt", "w") as g:
    for pair in random_pairs:
        f.write(pair[0])
        g.write(pair[1])

