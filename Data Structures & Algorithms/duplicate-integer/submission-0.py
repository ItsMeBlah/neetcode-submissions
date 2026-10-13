class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = set()

        for num in nums:
            current_len_freq = len(freq)
            freq.add(num)

            if current_len_freq == len(freq):
                return True
        return False