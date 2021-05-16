import urllib
import requests
from unittest import TestCase
import random


def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    
    return bookascii.split()
def counting_sort(idx, book = book_to_words(), length = len(book_to_words()), key_num = 256):
    to_return = [0] * length
    counts = [0] * (key_num + 1)
    for item in book:
        if len(item) > idx:
            counts[(item[idx]) + 1] +=1
        else:
            counts[0] += 1
    for i in range(len(counts)-1):
        counts[i + 1] += counts[i]
    for item in reversed(book):
        if len(item) > idx:
            index = (item[idx]) + 1
        else:
            index = 0
        to_return[counts[index] - 1] = item
        counts[index] -= 1
    
    return to_return

def max_length(book = book_to_words()):
    max = 0
    for word in book:
        
        if len(word) > max:
            max = len(word)
    return max


def radix_a_book(length = len(book_to_words()), book = book_to_words(), max_length = max_length(), key_num = 256):
   
    for idx in range(max_length - 1, -1, -1):
        book = counting_sort(idx, book = book, length = length, key_num = key_num)
    return book
    
################################################################################d
# TEST CASES
################################################################################

# simple test

def test_simple():
    tc = TestCase()
    test = [b'aba' , b'aaaa', b'acc', b'aaa', b'abb', b'bbb', b'ccca', b'ccc']
    print(f'Output is supposed to be: b\'aaa\', b\'aaaa\', b\'aba\', b\'abb\', b\'acc\', b\'bbb\', b\'ccc\', b\'ccca\'')
    print(radix_a_book(book = test, length = 8, max_length = 4))
    
    tc.assertEqual(radix_a_book(book = test, length = 8, max_length = 4), [b'aaa', b'aaaa', b'aba', b'abb', b'acc', b'bbb', b'ccc', b'ccca'])
# RR-fix (simple) test
# 10 points
def test_simple2():
    tc = TestCase()
    test2 = [b'horse' , b'banana', b'monkey', b'bonano', b'monkiy', b'hornse', b'grasshopper', b'catfish', b'batfish']
    print(f'Output is supposed to be: [b\'banana\', b\'batfish\', b\'bonano\', b\'catfish\', b\'grasshopper\', b\'hornse\', b\'horse\', b\'monkey\', b\'monkiy\'] ')
    print(radix_a_book(book = test2, length = 9, max_length = 11))
    tc.assertEqual(radix_a_book(book = test2, length = 9, max_length = 11),[b'banana', b'batfish', b'bonano', b'catfish', b'grasshopper', b'hornse', b'horse', b'monkey', b'monkiy'])
    
# LR-fix (simple) test
# 10 points
def test_book1():
    tc = TestCase()
    
    
    h = sorted(book_to_words())
    tc.assertEqual(h, radix_a_book())





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
    print('\n Radix Sort works flawlessly, the same as sorted()!')

if __name__ == '__main__':
    main()
