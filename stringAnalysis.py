#Greg Phillips
#9/6/17
#stringAnalysis.py

sentence = input("Enter a sentence here")
spaces = sentence.count(" ")
characters = len(sentence)
words = spaces+1 
letters = characters-spaces
print("Your sentence has", words, "words", characters, "Characters and", letters, "letters")

search = input("Enter a character to search for here")

