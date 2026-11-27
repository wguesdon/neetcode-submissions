class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # Store previously visited numbers as {number: index}

        for i, num in enumerate(nums):  # Iterate over indices and values
            complement = target - num  # Calculate the missing number

            if complement in seen:  # Check if complement exists in O(1) average time
                return [seen[complement], i]  # Return indices in ascending order

            seen[num] = i  # Store current number after checking to avoid self-matching

        return []  # Never reached because exactly one valid pair is guaranteed