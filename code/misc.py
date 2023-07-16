import re
from difflib import SequenceMatcher
import random

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def file2listGOC(pre_id2filename, post_id2filename, fileid):
    '''
    Process a list of paired files into a list of paired sentences.
    '''

    with open(pre_id2filename[fileid], 'r') as f:
        prestr = f.readlines()

    with open(post_id2filename[fileid], 'r') as f:
        poststr = f.readlines()

    removedQuota_post = "".join(poststr).replace("‘","'").replace("’","'")
    removedQuota_pre = "".join(prestr).replace("‘","'").replace("’","'")

    # This is for dirty txt
    removed_n_post = " ".join(removedQuota_post.split('\n')).strip()
    removed_n_pre = " ".join(removedQuota_pre.split('\n')).strip()

    poststr = " ".join(removed_n_post.split("\n"))
    prestr = " ".join(removed_n_pre.split("\n"))

    post_list = [i.strip()+"." for i in poststr.strip().split(". ")]
    pre_list = [i.strip()+"." for i in prestr.strip().split(". ")]
    
    return pre_list, post_list

def splitByMaxLength(text, minlength = 32, maxLength = 256):
    '''
    Split a long sentence into multiple sentences with a maximum length.
    :param text: a long sentence
    :param minlength: the minimum length of a sentence (default: 1)
    :param maxLength: the maximum length of a sentence (default: 128)
    :return: a list of sentences
    '''

    sentences = []
    currentSentence = ""
    for i in range(0, len(text)):
        currentChar = text[i]
        currentSentence += currentChar
        if len(currentSentence.strip()) >= minlength and re.match("[\r\n.?!]", currentChar):
            sentences.append(currentSentence)
            currentSentence = ""
        elif len(currentSentence.strip()) >= maxLength:
             # this code is rubbish but works (should have renamed i)
            lastIndexOfComma = currentSentence.rfind(",")
            if lastIndexOfComma == -1:
                lastIndexOfSpace = currentSentence.rfind(" ")
            else:
                lastIndexOfSpace = lastIndexOfComma
            sentences.append(currentSentence[0:lastIndexOfSpace])
            currentSentence = currentSentence[lastIndexOfSpace + 1:]
    if currentSentence != "":
        sentences.append(currentSentence)
    res = []
    for sentence in sentences:
        extractN = sentence.split("\n")
        for j in range(0, len(extractN)):
            if extractN[j] == "\n":
                res.append(extractN[j])
            else:
                res.append(extractN[j].strip())
    return list(filter(bool, res))


# write a function that randomly select subsequence pairs from a list of pairs
# for example: we have pairs ("hello, world thiss Junfan", "hello, world this is Junfan")
# we want to randomly select a subsequence pair ("world thiss Junfan", "world this is Junfan"), ("thiss Junfan", "this is Junfan") and so on
# the length of the subsequence is randomly selected from 1 to the length of the original sequence



# note that sometimes the words in the subsequence are not aligned, for example, ("Cha robh esan a' dolna bu mhiosa; cha robhsìon na b' fheàrr. ", "Cha robh esana' dol na bu mhiosa; cha robh sìon na b' fheàrr.")
# in this case, we need to align the subsequence pair
# for example, ("Cha robh esan a' dolna bu mhiosa", "Cha robh esana' dol na bu mhiosa") -> ("Cha robh esan a' dolna bu mhiosa", "Cha robh esana' dol na bu mhiosa")
# then we can randomly select a subsequence pair ("Cha robh esan a' dolna bu mhiosa", "Cha robh esana' dol na bu mhiosa") -> ("Cha robh esan a' dolna bu mhiosa", "Cha robh esana' dol na bu mhiosa")

def randomSubsequencePairAligned(pre_list, post_list):
    '''
    Randomly select a subsequence pair from a list of pairs.
    '''
    # randomly select a pair
    pair_index = random.randint(0, len(pre_list)-1)
    pre = pre_list[pair_index]
    post = post_list[pair_index]
    
    # randomly select a subsequence
    subsequence_length = random.randint(1, len(pre.split(" ")))
    subsequence = " ".join(pre.split(" ")[-subsequence_length:])
    
    # find the subsequence in the post
    post_subsequence = post.split(" ")[-subsequence_length:]
    post_subsequence = " ".join(post_subsequence)
    
    # align the subsequence
    aligned_subsequence, aligned_post_subsequence = align(subsequence, post_subsequence)
    
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
    aligned_post_subsequence = " ".join(post_subsequence_words[index:index+len(post_subsequence_words)])
    
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
    random_pairs = []
    while len(random_pairs) < num_pairs:
        pre, post = randomSubsequencePairAligned(pre_list, post_list)
        if pre != 0 and post != 0 and len(pre) >= min_length:
            random_pairs.append((pre, post))
    return random_pairs

with open("../processed/01_test_paired_only/postGOC_clean.txt", "r") as f:
    post_list = f.readlines()

with open("../processed/01_test_paired_only/preGOC_clean.txt", "r") as f:
    pre_list = f.readlines()



# random_pairs = generateRandomPairs(pre_list, post_list, num_pairs=3000000)

# # write to two files
# with open("../processed/04_test_rule_random_sample/preGOC.txt", "w") as f, open("../processed/04_test_rule_random_sample/postGOC.txt", "w") as g:
#     for pair in random_pairs:
#         f.write(pair[0])
#         g.write(pair[1])