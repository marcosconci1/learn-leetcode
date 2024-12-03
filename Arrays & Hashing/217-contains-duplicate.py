'''
 217. Contains Duplicate [https://leetcode.com/problems/contains-duplicate/description/]

You need to check if there are any repeated numbers in a list.
The list can have up to 100,000 elements, so your solution needs to be efficient.
The range of numbers is from -1 billion to 1 billion, so you can't rely on the order of the numbers, but you can use other techniques.

'''

def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    s = set()
    for i in nums:
        if(i in s):
            return print("true")
        s.add(i)
    return print("false")

nums = [1,2,3,1]
containsDuplicate(nums)