class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1]

        for i in range(len(nums)):
            if i >= len(nums) - 1:
                break

            prefix.append(nums[i]*prefix[-1])
            suffix.append(nums[len(nums)-1-i]*suffix[-1])

        for i in range(len(prefix)):
            prefix[i] = prefix[i] * suffix[len(suffix)-i-1]

        return prefix