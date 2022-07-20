#Pangram is a sentence that uses all the letters in the alphabet
#Test should check for case sensitive
#Test should check for missing characters
#Test should check for underscores 
#Test should check if the string is empty
#Test should check for the length 26 

def is_pangram(sentence):
    pass

    letters = set()

    for character in sentence:
        if character.isalpha():
            letters.add(character.lower())
    return len(letters) == 26 