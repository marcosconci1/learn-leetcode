from collections import Counter

def isAnagram(s, t) -> bool:
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
        False

    return Counter(s) == Counter(t)
    
print(isAnagram("anagram", "nagaram"))
        