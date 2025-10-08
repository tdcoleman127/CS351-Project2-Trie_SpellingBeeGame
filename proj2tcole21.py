# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 14:37:19 2025

@author: Trenton C
"""
from sbtrie import SBTrie 

# the following functions are to exist with the parameters as written
# the autograder may call these functions

def getNewDictionary(sbt, filename):
  # enter needed code here for command 1
  sbt.potentialWords.clear()
  sbt.potentialWords.getFromFile(filename)
  pass

def updateDictionary(sbt, filename):
  # enter needed code here for command 2
  
  # Try and open it
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
      sbt.insert(line.strip())
      
  file.close()
  return True

def setupLetters(sbt, letters):
  # enter needed code here for command 3
  count = 0
  letterSet = set()
  for l in letters:
     if l.isalpha():
        count += 1
        letterSet.add(l)

  if(len(letterSet) != 7):
    print("Invalid letter set")
  else:
    sbt.centralLetter = ''
    sbt.allowedLetters = []
    sbt.currentWords.clear()
    sbt.currentScore = 0
    sbt.foundPangram = False
    sbt.foundBingo = False

    sbt.centralLetter = letters[0]
    for i in range(1, len(letters)):
      if letters[i].isalpha():
        sbt.allowedLetters.append(letters[i].lower())

def showLetters(sbt):
  # enter needed code here for command 4
  print("Central Letter: " + sbt.centralLetter)
  print("6 Other Letters")
  print(*sbt.allowedLetters, sep=",")
  
def attemptWord(sbt, word):
  # enter needed code here for command 5
  result = sbt.isNewSBWord(word)
  if result == -1:
    print("word is too short")
  elif result == -2:
    print("word is missing central letter") 
  elif result == -3:
    print("word contains invalid letter")
  elif result == -4:
    print("word is not in the dictionary")
  elif result == -5:
    print("word has already been found")
  else:
    # Add to score
    sbt.currentScore += result
    # Increase numWord count
    sbt.currentWords.numWords += 1
    sbt.currentWords.insert(word)
    combined_string = "found " + word + " " + str(result) + " points, " + str(sbt.currentWords.wordCount()) + " words found, total " + str(sbt.currentScore) + " points"
    if(sbt.foundPangram):
     combined_string += ", Pangram found"
    if(sbt.foundBingo):
      combined_string += ", Bingo scored"
    print(combined_string)
  pass

def showFoundWords(sbt):
  # enter needed code here for command 6
  combined_string = str(sbt.currentWords.wordCount()) + " words found, total " + str(sbt.currentScore) + " points"
  if(sbt.foundPangram):
     combined_string += ", Pangram found"
    
  if(sbt.foundBingo):
     combined_string += ", Bingo scored"
    
  print(combined_string)

def showAllWords(sbt):
  # enter needed code here for command 7

  finalList = sbt.sbWords(sbt.centralLetter, sbt.allowedLetters)
  combined_string = ""
  for word in finalList:
    combined_string = word + " " + str(len(word))
    if(sbt.foundPangram):
      combined_string += " Pangram"
    print(combined_string)
    
  if(sbt.foundBingo):
     print("Bingo scored")
  pass

def displayCommands():
  print( "\nCommands are given by digits 1 through 9\n")
  print( "  1 <filename> - read in a new dictionary from a file")
  print( "  2 <filename> - update the existing dictionary with words from a file")
  print( "  3 <7letters> - enter a new central letter and 6 other letters")
  print( "  4            - display current central letter and other letters")
  print( "  5 <word>     - enter a potential word")
  print( "  6            - display found words and other stats")
  print( "  7            - list all possible Spelling Bee words from the dictionary")
  print( "  8            - display this list of commands")
  print( "  9            - quit the program")
  print()


def spellingBee():
  print("Welcome to Spelling Bee Game")
  
  sbt = SBTrie()

  displayCommands()

  while (True):
    line = input ("cmd> ")
    command = line[0]
    #print ("Debug 0:" + line + "***" + command + "***")
    
    # clear input from any previous value
    args = ""

    
    if(command == '1'):
        # args = line[1:].strip()
        try:
          args = line[1:].strip()
        except EOFError:
            print("No interactive input in the autograder environment.")
            return
        if not args:
            print("Empty filename.")
            return
        #print ("Debug 1:" + args + "***")
        getNewDictionary(sbt, args)

    if(command == '2'):
        try:
          args = line[1:].strip()
        except EOFError:
            print("No interactive input in the autograder environment.")
            return
        if not args:
            print("Empty filename.")
            return
        #print( "Debug 2:" + args + "***")
        updateDictionary(sbt, args)
        
    if(command == '3'):
        args = line[1:].strip()
        #print( "Debug 3:" + args + "***")
        setupLetters(sbt, args)


    if(command == '4'):
        showLetters(sbt)

    if(command == '5'):
        args = line[1:].strip()
        #print ( "Debug 5:" + args + "***")
        attemptWord(sbt, args)

    if(command == '6'):
        showFoundWords(sbt)

    if(command == '7'):
        showAllWords(sbt)

    
    if(command == '8' or command == '?'):
        displayCommands()
    
    if(command == '9' or command == 'q'):
        break
    

  return
  
if __name__ == "__main__":
    spellingBee()