# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):  
    sorted_word = sorted(word)
    sorted_anagram = sorted(anagram)
    return True

word = input("Enter word: ")
anagram =input("Enter word: ")

if(sorted(word)== sorted(anagram)):
       print("True")
else:
       print("False")  


 