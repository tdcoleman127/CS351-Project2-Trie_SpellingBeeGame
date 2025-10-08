# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 15:17:47 2025

@author: Trenton C
"""
from trie import Trie

class SBTrie(Trie):
    """ A class for the Spelling Bee Trie """
    def __init__ (self):
        self.root = Trie()
        self.insertDataMember = 0
        self.centralLetter = ''
        self.allowedLetters = []
        self.potentialWords = Trie()
        self.currentWords = Trie()
        self.currentScore = 0
        self.foundPangram = False
        self.foundBingo = False
        self.numWords = 0

    def getLetters(self) -> str:
        letterString = self.centralLetter + ""
        letSet = sorted(self.allowedLetters)
        for let in letSet:
            letterString += let
        return letterString
    
    def isNewSBWord(self, word: str) -> int:
        if(self.currentWords.search(word) == False):
            if(self.isPangram(word)):
                return 7
            elif(len(word) == 4):
                return 1
            else:
                return 1 * len(word)
            
        # -1: word is too short 
        if(len(word) < 4):
            return -1
        # -2: word is missing central letter
        if self.centralLetter not in word:
            return -2
        # -3: word contains at least one invalid letter
        for c in word:
            if c.isalpha() == False or c == ' ':
                return -3
        # 4: word is not in the dictionary 
        if word not in self.potentialWords.words():
            return -4
        # -5: word has already been found 
        if word in self.currentWords.words():
            return -5
        pass

    def isPangram(self, word: str) -> bool:
        # Check if the word contains all 7 of the current letters
        # Check if the word length is 7
        if(len(word) != 7):
            return False
        currentLetters = self.getLetters()
        currLetSet = set(currentLetters)
        wordSet = set(word)
        return wordSet == currLetSet

    def hasBingo(self) -> bool:
        currentLetters = self.getLetters()
        if len(currentLetters) != 7:
            return False
        # If there isn't a word in the currentWords Trie that begins with
        # one of the letters, return False
        bingoList = []
        for c in currentLetters:
            # Faster method: Use a function to find a word with a prefix in Trie
            # Standard method: Look in the Trie's word list and check the first char
            for word in self.currentWords.trieWords:
                if word[0] == c:
                    # Add it to a list of characters, should have the same content as currentLetters list
                    bingoList.append(word[0])

        if(bingoList != currentLetters):
            return False
        return True

    def getFoundWords(self):
        return self.currentWords.words()

    def sbWords(self, centralLetter: str, otherLetters: str):
        finalList = []

        # Word Criteria:
        # - word has to be at least 4 letters long (len >= 4)
        # - word has to have the central letter
        # - words can only have the other letters in the otherLetters string

        for word in self.currentWords.words():
            if(len(word) >= 4 and centralLetter in word):
                    for c in word:
                        if c in otherLetters:
                            finalList.append(word)

        return finalList