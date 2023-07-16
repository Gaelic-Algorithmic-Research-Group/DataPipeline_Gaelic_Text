# from nlp.similar import *
import argparse
import unittest
import random
import os
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

parser = argparse.ArgumentParser()                                               

parser.add_argument("--filenames", "-f", type=str, required=True)
# parser.add_argument("--postGOC_file", "-post", type=str, required=True)
args = parser.parse_args()

preGOC, postGOC = args.filenames.split(" ")
TESTPREGOC_FILENAME = os.path.join(os.path.dirname(__file__), preGOC)
TESTPOSTGOC_FILENAME = os.path.join(os.path.dirname(__file__), postGOC)


class demoTest(unittest.TestCase):

    random_nums = None

    def setUp(self):
        self.prefile = open(TESTPREGOC_FILENAME)
        self.prelines = self.prefile.readlines()
        self.postfile = open(TESTPOSTGOC_FILENAME)
        self.postlines = self.postfile.readlines()
        self.random_nums = [random.randint(0, len(self.postlines)-1), random.randint(0, len(self.postlines)-1), random.randint(0, len(self.postlines)-1)]

    def tearDown(self):
        self.random_nums = None
        self.prefile.close()
        self.postfile.close()

    # @classmethod
    # def setUpClass(cls):
    #     cls.testfile = open(TESTDATA_FILENAME)
    #     cls.testdata = self.testfile.read()
    #     cls.random_nums = random.randint(1, len())

    # @classmethod
    # def tearDownClass(cls):
    #     cls.random_nums = None
    #     self.testfile.close()
    def test_linenum(self):
        print("\n")
        print("Test if line nums are equal?")
        self.assertEqual(len(self.prelines), len(self.postlines))
    def test_simliarity_50(self):
        print("\n")
        print("Test lines similarity - 50%")
        random_nums = self.random_nums
        print(random_nums)
        print(self.prelines[random_nums[0]])
        print(self.postlines[random_nums[0]])
        self.assertTrue(similar(self.prelines[random_nums[0]],self.postlines[random_nums[0]])>0.5)
        self.assertTrue(similar(self.prelines[random_nums[1]],self.postlines[random_nums[1]])>0.5)
        self.assertTrue(similar(self.prelines[random_nums[2]],self.postlines[random_nums[2]])>0.5)
    def test_simliarity_70(self):
        print("\n")
        print("Test lines similarity - 70%")
        random_nums = self.random_nums
        print(random_nums)
        print(self.prelines[random_nums[0]])
        print(self.postlines[random_nums[0]])
        self.assertTrue(similar(self.prelines[random_nums[0]],self.postlines[random_nums[0]])>0.7)
        self.assertTrue(similar(self.prelines[random_nums[1]],self.postlines[random_nums[1]])>0.7)
        self.assertTrue(similar(self.prelines[random_nums[2]],self.postlines[random_nums[2]])>0.7)
    def test_simliarity_80(self):
        print("\n")
        print("Test lines similarity - 80%")
        random_nums = self.random_nums
        print(random_nums)
        print(self.prelines[random_nums[0]])
        print(self.postlines[random_nums[0]])
        self.assertTrue(similar(self.prelines[random_nums[0]],self.postlines[random_nums[0]])>0.8)
        self.assertTrue(similar(self.prelines[random_nums[1]],self.postlines[random_nums[1]])>0.8)
        self.assertTrue(similar(self.prelines[random_nums[2]],self.postlines[random_nums[2]])>0.8)

if __name__ == '__main__':
    unittest.main(argv=['filenames'], exit=False)
