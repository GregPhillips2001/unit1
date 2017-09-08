#Greg Phillips
#9/6/17
#stringAnalysis.py

sentence = input("Enter a sentence here ")
spaces = sentence.count(" ")
characters = len(sentence)
words = spaces+1 
letters = characters-spaces
print("Your sentence has", words, "words", characters, "Characters and", letters, "letters")
sentence2 = sentence.lower()

search = input("Enter a character to search for here ")
numberOfCharacter = sentence2.count(search)
print("Your sentence has", numberOfCharacter, "of the character", search)

word = input("Enter a word to search for here ")
numberOfWord = sentence2.count(word)
print("Your sentence has", numberOfWord, "of the word", word)
