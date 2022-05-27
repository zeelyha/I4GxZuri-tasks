# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename) as f:
        contents = f.read()
    
    return contents


def count_words(filename):
    text = read_file_content(filename)
    # [assignment] Add your code here
    
    split_text = text.split()
    words = {}
    for i in split_text:
        i= i.lower()
        if i in words:
            words[i] += 1
        else:
            words[i] = 1
    return words    


print(count_words("story.txt"))