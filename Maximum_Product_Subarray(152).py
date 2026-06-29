class Solution:
    def maxProduct(self, nums):
        max_prod = nums[0]
        curr_max = nums[0]
        curr_min = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            # Negative number max aur min ko swap kar sakta hai
            temp_max = max(num, curr_max * num, curr_min * num)
            temp_min = min(num, curr_max * num, curr_min * num)

            curr_max = temp_max
            curr_min = temp_min

            max_prod = max(max_prod, curr_max)

        return max_prod
