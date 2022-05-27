# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    unspaced_word = word.replace(" ", "")
    unspaced_anagram = anagram.replace(" ", "")
    
    #striped_anagram = anagram.strip()
    if sorted(unspaced_word.lower()) == sorted(unspaced_anagram.lower()):
        return True
    else:
        return False    
    

print(find_anagram("I am gone","Name I go"))