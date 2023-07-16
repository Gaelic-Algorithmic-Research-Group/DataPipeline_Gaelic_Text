
from pathlib import Path
import random
import os

cwd = os.getcwd()
cwd = Path(cwd) / 'data' / 'DataPipeline_Gaelic_Text' 
# part1 - generate list of nouns with GOC format
def intersect_two_txt(file1,file2,output_path):
    """
    generate a set contains a intersection of two files, and save it to new_file, without using with inside with
    """
    with open(file1,'rb') as f1:
        decodedf1 = f1.read().decode('utf-8')
    
    with open(file2,'rb') as f2:
        decodedf2 = f2.read().decode('utf-8')

    set1 = set(decodedf1.splitlines())
    set2 = set(decodedf2.splitlines())
    new_set = set1 & set2

    with open(output_path,'w', encoding="utf-8") as f3:
        for i in new_set:
            f3.write(i+'\n')


dictionary_goc = cwd / 'rowdata/dictionary/20220816_gd_GB/glan-goc.txt'
dictionary_nouns = cwd / 'rowdata/dictionary/20220816_singular_nominative_nouns.txt'
intersect_nouns = cwd / 'intermediate/20220816_intersect_nouns.txt'
intersect_two_txt(dictionary_goc,dictionary_nouns,intersect_nouns)

# part2 - generate sentence using intersect_nouns with GOC format

# Any of these, Number above 20, Any noun on the list, Any of these,Any noun on the list
# Tha,,air,
# Bha,,aig,
# Bidh,,,
# Bhiodh,,,
# Chan,,eil,
# Cha,,robh,
# Cha,,bhi,
# Cha,,bhiodh,

# For example
# Tha 29 bò air achadh
# Chan eil 30034 cat aig boireannach

def generate_sentence(intersect_nouns, number_of_sentences, output_path):
    """
    generate sentence using intersect_nouns baded on the csv template below with 5 columns

    row[0] + a number > 20 + noun + row[3] + noun

    A template file is provided below:
    Any of these, Number above 20, Any noun on the list, Any of these, Any noun on the list
    Tha,,,air,
    Bha,,,aig,
    Bidh,,,,
    Bhiodh,,,,
    Chan,,,eil,
    Cha,,,robh,
    Cha,,,bhi,
    Cha,,,bhiodh,

    For example
    Tha 29 bò air achadh
    Chan eil 30034 cat aig boireannach
    
    step1: select a random row: Tha,,air,
    step2: generate a sentence using the row above: Tha + noun + air + noun
    """
    with open(intersect_nouns,'r') as f:
        nouns = f.read().splitlines()
    # select two random nouns from the list
    
    with open(template,'r', encoding="utf-8") as t:
        rows = t.read().splitlines()

    with open(output_path,'a') as f:
        for i in range(number_of_sentences):
            # random selection
            random_row = random.choice(rows)
            number = random.randint(21,99)
            noun1 = random.choice(nouns)
            noun2 = random.choice(nouns)
            row1, _ , _, row3,_ = random_row.split(',')

            # sentence generation
            if row3:
                sentence = row1 + ' ' + str(number) + ' ' + noun1 + ' ' + row3 + ' ' + noun2
            else:
                sentence = row1 + ' ' + str(number) + ' ' + noun1 + ' ' + noun2

            f.write(sentence+'\n')


if __name__ == '__main__':
    template = cwd / Path('rowdata/20220816_template_num_sentence_generation')
    output_path = cwd / Path('processed/postGOC/simulated/20220816_num_sentences.txt')
    generate_sentence(intersect_nouns, 100, output_path)
    print('done')