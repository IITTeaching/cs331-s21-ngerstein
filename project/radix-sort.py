import urllib
import requests
from unittest import TestCase
import random


################################################################################
# EXTENSIBLE HASHTABLE
################################################################################
class HashTable:

    def __init__(self, n_buckets=256, fillfactor=1):
        self.n_buckets = n_buckets
        self.fillfactor = fillfactor
        self.buckets = [[None]] * n_buckets
        self.nitems = 0

    def __getitem__(self,  key):
        # BEGIN_SOLUTION
        if self.buckets[key] != None:    
            return self.buckets[key]
        raise KeyError
        # END_SOLUTION

    def __setitem__(self, key, value):
        # BEGIN_SOLUTION
        pos = key
        self.nitems += 1
        if self.buckets[pos] == [None]:
            self.buckets[pos] = [(key, value)]
        else:
            self.buckets[pos].append((key, value))
        # END_SOLUTION


    def __contains__(self, key):
        try:
            _ = self[key]
            return True
        except:
            return False

    def __len__(self):
        return self.nitems

    def __bool__(self):
        return self.__len__() != 0

    def __iter__(self):
        ### BEGIN SOLUTION
        for i in range(self.n_buckets):
            if self.buckets[i]:
                for item in self.buckets[i]:
                    if item:
                        yield item
        ### END SOLUTION

    def items(self):
        ### BEGIN SOLUTION
        
        for i in range(self.n_buckets):
            if self.buckets[i]:
                for item in self.buckets[i]:
                    if item:
                        yield item
        ### END SOLUTION

    def __str__(self):
        return '{ ' + ', '.join(str(k) + ': ' + str(v) for k, v in self.items()) + ' }'

    def __repr__(self):
        return str(self)


def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    
    return bookascii.split()

def max_length(book = book_to_words()):
    max = 0
    for word in book:
        
        if len(word) > max:
            max = len(word)
    return max


def fill_buckets(idx = 0, book = book_to_words()):
    
    data = HashTable()
    for word in book:
        if len(word) < idx + 1:
            data[0] = word
        else:
            data[word[-1 -idx]] = word
    return data


def LSD_sort(idx, data):
    
    newdata = HashTable()
    
    for items in data:
        
        if len(items[1]) < idx + 1:
            newdata[0] = items[1]
        else:
            byte = items[1]
            newdata[byte[-1 -idx]] = items[1]
    return newdata

def radix_a_book(book = book_to_words(), key = None, idx = None):
    
    max = max_length(book)
    newbuckets = fill_buckets(book = book)
    for i in range(max - 1):
        newbuckets = LSD_sort(i + 1, newbuckets)
    if (key == None) and (idx == None):
        return newbuckets
    elif (key != None) and (idx != None):
        return newbuckets[key][idx]
    elif (key != None) and (idx == None) :
        return newbuckets[key]
    


################################################################################d
# TEST CASES
################################################################################

# simple test

def test_simple():
    tc = TestCase()
    test = [b'aaa' , b'aba', b'acc', b'abb', b'bbb', b'ccc', b'ccca']
    print(f'Output is supposed to be: b\'aaa\', b\'aba\', b\'abb\', b\'acc\', b\'bbb\', b\'ccc\', b\'ccca\'')
    print(radix_a_book(book = test))
    
    tc.assertEqual(radix_a_book(book = test, key = 0, idx = 3), (0, b'acc'))

# RR-fix (simple) test
# 10 points
def test_simple2():
    tc = TestCase()
    test2 = [b'horse' , b'banana', b'monkey', b'bonano', b'monkiy', b'hornse', b'grasshopper', b'catfish', b'batfish']
    print(f'Output is supposed to be: 0: b\'horse\', 0: b\'banana\', 0: b\'bonano\', 0: b\'hornse\', 0: b\'monkey\', 0: b\'monkiy\', 0: b\'batfish\', 0: b\'catfish\' 103: b\'grasshopper\' ')
    print(radix_a_book(test2))
    tc.assertEqual(radix_a_book(book = test2, key = 0, idx = 3), (0, b'hornse'))
    tc.assertEqual(radix_a_book(book = test2, key = 0, idx = 1), (0, b'banana'))
    tc.assertEqual(radix_a_book(book = test2, key = 0), [(0, b'horse'), (0, b'banana'), (0, b'bonano'), (0, b'hornse'), (0, b'monkey'), (0, b'monkiy'), (0, b'batfish'), (0, b'catfish')])
# LR-fix (simple) test
# 10 points
def test_book1():
    tc = TestCase()
    t = b'h'

    a = radix_a_book(key = 0, idx = 1000)
    b = radix_a_book(key = 0, idx = 3000)
    char1 = a[1]
    char2 = b[1]
    
    print(f'a: {a} should come before b: {b}')
    tc.assertEqual(radix_a_book(key = t[0], idx = 0), (104, b'https://www.gutenberg.org/8/84/'))
    tc.assertTrue(char2[0] > char1[0])





################################################################################
# TEST HELPERS
################################################################################
def say_test(f):
    print(80 * "#" + "\n" + f.__name__ + "\n" + 80 * "#" + "\n")

def say_success():
    print("----> SUCCESS")

################################################################################
# MAIN
################################################################################
def main():
    for t in [test_simple,
              test_simple2,
              test_book1]:
        say_test(t)
        t()
        say_success()
    print(80 * "#" + "\nALL TEST CASES FINISHED SUCCESSFULLY!\n" + 80 * "#")
    print('\n Radix Sort works flawlessly!')

if __name__ == '__main__':
    main()
