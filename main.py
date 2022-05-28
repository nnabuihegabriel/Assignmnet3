# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = input('Please enter a word: ')
    
    sorted_str1 = sorted(word)
    sorted_str2 = sorted(anagram)
    
    if (sorted_str1 == sorted_str2):
        print('True') 
    else:
       print('False')
        
find_anagram('word', 'anagram')

