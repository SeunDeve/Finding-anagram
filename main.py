# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    arr1 = list(word)
    arr1.sort()
    arr2 = list(anagram)
    arr2.sort()
    if arr1 == arr2:
        return True
    else:
        return False    

print(find_anagram('below', 'elbow'))

