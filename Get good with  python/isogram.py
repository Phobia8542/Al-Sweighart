#Isogram is a word or phrase that containers letters that occur the same amount of times
#Test should check for duplicates of non-letter characters (numbers, symbols, etc)
#Test should check for duplicates of made up words
#Test should check for duplicates of mixed cased words (ExAmPLe)
#Test should check for duplicates of words with hyphens
#Test should check for duplicates of only lower case characters
def is_isogram(word):
    
    letters = set()
    
    for character in word:

        letters.add(character)
        return True