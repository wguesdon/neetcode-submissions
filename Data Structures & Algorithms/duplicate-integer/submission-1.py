class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:  # O(1) on average
                return True  # first repeat: stop early
            seen.add(num)
        return False  # the loop finished, so no value repeats