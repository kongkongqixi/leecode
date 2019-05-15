class Solution:
    def threeSumClosest(self, nums, target):
        if len(nums) < 2:
            return False
        nums.sort()
        print(nums)
        value = abs(nums[0] + nums[1] + nums[2] - target)

        result = nums[0] + nums[1] + nums[2]
        if value == 0:
            return result
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            if nums[i] + nums[k - 1] + nums[k] <= target:
                if abs(nums[i] + nums[k - 1] + nums[k] - target) < value:
                    result = nums[i] + nums[k - 1] + nums[k]
                    value = abs(nums[i] + nums[k - 1] + nums[k] - target)
                continue
            if nums[i] + nums[j] + nums[j + 1] >= target:
                if abs(nums[i] + nums[j] + nums[j + 1] - target) < value:
                    result = nums[i] + nums[j] + nums[j + 1]
                    value = abs(nums[i] + nums[k - 1] + nums[k] - target)
                continue
            while j < k:
                temp_value = nums[j] + nums[k] + nums[i] - target
                if abs(temp_value) < value:
                    result = nums[i] + nums[j] + nums[k]
                    value = abs(temp_value)
                if temp_value > 0:
                    k -= 1
                elif temp_value == 0:
                    return result
                else:
                    j += 1
        return result
s = Solution()
print(s.threeSumClosest([0,2,1,-3], 1))




        # for i in range(3, len(nums)):
        #     a1 = 0
        #     if a > abs(nums[i]+y+z-target):
        #         a1 = abs(nums[i]+y+z-target)
        #     if abs(x+nums[i]+z-target) > a1:
        #         a1 =




