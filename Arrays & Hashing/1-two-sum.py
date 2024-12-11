def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    seen = {}  # Dictionary to store numbers and their indices
    
    for i in range(len(nums)):
        complement = target - nums[i]  # Calculate the complement
        
        # Check if the complement is already in the dictionary
        if complement in seen:
            return [seen[complement], i]  # Return the indices of the two numbers
        
        # Add the current number to the dictionary
        seen[nums[i]] = i


# Test cases
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))  # Output: [0, 1]

nums = [3, 3]
target = 6
print(twoSum(nums, target))  # Output: [0, 1]

nums = [3, 2, 4]
target = 6
print(twoSum(nums, target))  # Output: [1, 2]
