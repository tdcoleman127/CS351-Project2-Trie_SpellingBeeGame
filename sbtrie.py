# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 15:17:47 2025

@author: troy
"""
from trie import Trie

class SBTrie(Trie):
    """ A class for the Spelling Bee Trie """
    def __init__ (self):
        self.insertDataMember = 0
        self.centralLetter = ''
        self.allowedLetters = []
        self.potentialWords = Trie()
        self.currentWords = Trie()
        self.currentScore = 0
        self.foundPangram = False
        self.foundBingo = False

    def getLetters(self) -> str:
        letterString = self.centralLetter + ""
        letSet = sorted(self.allowedLetters)
        for let in letSet:
            letterString += let
        return letterString
    
    def isNewSBWord(self, word: str) -> int:
        pass

    def isPangram(SBTrie, word: str) -> bool:
        pass

    def hasBingo (SBTrie) -> bool:
        pass

    def getFoundWords(self) -> [str]:
        pass

    def sbWords(centralLetter: str, otherLetters: str) -> [str]:
        pass
    
    def addFoundWord():
        pass

def test():
    sb = SBTrie()
    print(sb.getLetters)