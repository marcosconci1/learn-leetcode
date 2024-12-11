strs = ["eat","tea","tan","ate","nat","bat"]

def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    anagram_map = {}
    
    for s in strs:
        key = ''.join(sorted(s))
        if key not in anagram_map:
            anagram_map[key] = []
        anagram_map[key].append(s)
        
    return list(anagram_map.values())
        
print(groupAnagrams(strs))
