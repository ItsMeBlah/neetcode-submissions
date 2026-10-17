class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1 or nums is None:
            return 0

        set_nums = list(set(nums))
        sorted_nums = sorted(set_nums)
        previous_num = sorted_nums[0]
        last_count = 1
        count = 1
        

        for i in range(1, len(sorted_nums)):
            temp = sorted_nums[i] - previous_num
            previous_num = sorted_nums[i]

            if temp != 1:
                if count > last_count:
                    last_count = count

                count = 1
                continue

            count += 1

        if last_count > count:
            count = last_count

        return count 