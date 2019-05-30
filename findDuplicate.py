class Solution:
    def findDuplicate(self, nums) -> int:
        if len(nums) == 0 or len(nums) == 1:
            return -1
        while nums[0] != nums[nums[0]]:
            temp = nums[nums[0]]
            nums[nums[0]] = nums[0]
            nums[0] = temp
        return nums[0]
s = Solution()
print(s.findDuplicate([1,3,4,2,4]))




