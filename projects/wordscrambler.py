# Make a function that scrambles a string and return the scrambled string

import random 
scrambledword = ""
def wordscrambler(word):
    n = list(word)
    
    for char in range(len(n)):
        
        letter = n.pop(random.randint(0 , len(n) - 1))
        
        scrambledword += letter
        
    return "".join(scrambledword)

print(wordscrambler("test"))




     
        
     
    
    
    # take the letters in the word and randomly pick one and return it until all are done

print(wordscrambler("test"))
# print(popped_name.pop(index))
