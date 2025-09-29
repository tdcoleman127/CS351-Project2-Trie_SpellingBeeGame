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
        self.trieList = []
        self.numWords = 0
        
        
    def getFromFile(self, filename:str) -> bool:

        # # Make sure the filename wasn't empty:

        # if not filename:
        #     print("Empty filename.")
        #     return False

        # # Try and open it
        # try:
        #     file = open(filename, 'r')
        # except EOFError:
        #     print("No interactive input in the autograder environment.")
        #     return False
        
        # # Put each line into the file
        # for line in file:
        #     self.trieList.append(line)
            
        # file.close()
        # return True
        pass
        
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
        # pass

    #Citing Professor Tryo's code from 9/25 lecture on Trie with static list of children
    def insert(self, word:str) -> bool:
        currNode = self.root
        buildingWord = ""
        # Base case: Word already exists
        if(currNode.isWord):
            return False
        
        # For each character in the given word
        for ch in word:
            # If a character isn't a letter
            if(ch.isalpha()):
                return False
            # Find the alphabetical index of the character
            ind = ord(ch.lower()) - 97
            # If it's not in the current 
            if currNode.children([ind] == None):
                currNode.children[ind] = Node(ch.lower())
            # Move to the next character in the word
            buildingWord += ch
            currNode = currNode.children[ind]
            
        currNode.isWord = True
        self.numWords = self.numWords + 1
        self.trieList.append(buildingWord)
        return True

    # Search should find or not find a legit "word" no matter what
    def search(self, word:str) -> bool:
        currNode = self.root
        for ch in word:
            ind = ord(ch.lower()) - 97
            if currNode.children[ind] == None:
                return False
            else:
                currNode = currNode.children[ind]
        return currNode.isWord

    
    def remove(self, word:str) -> bool:
        currNode = self.root
        # Go through the word, try to find it in the tree
        for ch in word:
            ind = ord(ch.lower()) - 97
            currNode = currNode.children[ind]

        if currNode.isWord == False:
           return False
        
        currNode.isWord = False
        self.numWords = self.numWords - 1
        self.trieList.remove(word)
        return True
    
    def clear(self) -> bool:
        words = self.words()
        for w in words:
            self.remove(w)
        return True
    
    def wordCount(self) -> int:
        return self.numWords
    
    def words(self) -> str:
        self.trieList = sorted(self.trieList)
        return self.trieList
        # pass

print("Hi father")