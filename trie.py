# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 15:22:23 2025

@author: Trenton C
"""

class Node:
    def __init__(self, ch=0, isWord=False):
        self.children = [None] * 26
        self.char = ""
        self.isWord = isWord

class Trie:
    """ A class for the Trie """
    def __init__ (self):
        self.root = Node("root")
        self.trieWords = []
        self.numWords = 0
        
        
    def getFromFile(self, filename:str) -> bool:
        if not filename:
            print("Empty filename.")
            return False
        try:
            file = open(filename, 'r')
        except (FileNotFoundError, IOError):
            print("Error occurred opening file")
            return False
        # Put each line into the file
        for line in file:
            self.insert(line)
        
        file.close()
        return True

    # Citing Professor Troy's code from 9/25 lecture on Trie with static list of children
    def insert(self, word:str) -> bool:
        if(self.root == None):
            self.root = Node("root")

        currNode = self.root
        buildingWord = ""
        # Base case: Word already exists
        for ch in word:
            if ch.isalpha() == False:
                # print("Cannot add " + word + " with non-alpha char " + ch)
                return False
            
        # Cannot add word already in Trie
        if(self.search(word) == True):
            return False
        
        # Make word lowercase
        word.lower()
        
        # For each character in the given word
        for ch in word:
            # Find the alphabetical index of the character
            ind = ord(ch.lower()) - 97
            # If it's not in the current 
            if currNode.children[ind] == None:
                currNode.children[ind] = Node(ch.lower())
            # Move to the next character in the word
            buildingWord += ch
            currNode = currNode.children[ind]
            
        currNode.isWord = True

        # Increment numWords and add it to trieWords
        self.numWords = self.numWords + 1
        self.trieWords.append(buildingWord)
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
        # Perform a lazy deletion of a Trie word
        currNode = self.root
        if(self.search(word) == False or word not in self.trieWords):
            return False
        
        for ch in word:
            ind = ord(ch.lower()) - 97
            currNode = currNode.children[ind]

        # Lazily delete word
        currNode.isWord = False

        self.numWords = self.numWords - 1
        self.trieWords.remove(word)
        return True
    

    def clear(self) -> bool:
        # print("Clearing tree...")
        if(self.numWords == 0):
            return False
        
        # Resetting parameters
        self.root.children = [None] * 26
        self.trieWords = []
        self.numWords = 0

        return self.numWords == 0
    
    def wordCount(self) -> int:
        # O(1) return of current word count
        return self.numWords
    
    def words(self) -> str:
        if(self.trieWords == None):
            return []
        self.trieWords = sorted(self.trieWords)
        return self.trieWords