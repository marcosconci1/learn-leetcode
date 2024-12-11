nums = [1, 1, 1, 2, 2, 3]
k = 2

def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """

    freq = {}

    for i in nums:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    # Return the k most frequent elements
    return sorted(freq, key=freq.get, reverse=True)[:k]
    
print(topKFrequent(nums, k))
