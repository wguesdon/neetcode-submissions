class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Anagrams must have the same number of characters
        if len(s) != len(t):
            return False

        # Dictionary to store how many times each character appears
        counts = {}

        # Step 1: Count each character in s
        for ch in s:
            # get(ch, 0) returns the current count, or 0 if not found
            counts[ch] = counts.get(ch, 0) + 1

        # Step 2: Subtract the counts using characters from t
        for ch in t:
            # If a character in t was never in s, not an anagram
            if ch not in counts:
                return False

            # Decrease the count because we found a matching character
            counts[ch] -= 1

            # If count becomes negative, t has too many of this character
            if counts[ch] < 0:
                return False

        # All characters matched with the correct frequencies
        return True