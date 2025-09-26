# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 15:22:23 2025

@author: Trenton C
"""

class Node:
    def __init__(self):
        self.children = [None] * 26
        self.char = ""
        # What determines 
        self.isWord = False


class Trie:
    """ A class for the Trie """
    def __init__ (self):
        self.root = Node("root")

        
    def getFromFile():

        # functions for Step 1
# def getFrequencyCounts(fname):
#     # Intializing dictionary for frequency counts
#     myDict = {}

#     # Open file

#     file = open(fname, 'r')
    
#     # Read file for each character in each line
#     for line in file:
#         for char in line:
#             if char not in myDict:
#                 # if char not found, create key and give value 1
#                 myDict[char] = 1
#             else:
#                 # if found, increment frequency value
#                 myDict[char] += 1
#     file.close()
#     print("The dictionary of frequency counts for " + fname + " is: ")
    
#     # Sorting dictionary values by value, ascending
#     newDict = dict(sorted(myDict.items(), key=lambda x:x[1]))
#     print(newDict)
#     return newDict
        pass
    
    def insert():
        pass
    
    def remove():
        pass
    
    def clear():
        pass
    
    def wordCount():
        pass
    
    def words():
        pass