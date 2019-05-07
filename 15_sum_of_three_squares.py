class Solution:
    def threeSum1(self, nums):
        nums.sort()
        result = []
        len_num = len(nums)

        if len_num < 3 or nums[0] > 0 or nums[len_num-1] < 0:
            return []

        if nums[0] == nums[len_num - 1] == 0:
            return [[0, 0, 0]]

        if (nums[0] == 0 and nums[2] == 0) or (nums[len_num-3] == 0 and nums[len_num-1] == 0):
            return [[0,0,0]]

        j1 = 0
        i = 0
        len_zero = 0
        for z, num in enumerate(nums):
            if num <= 0:
                j1 = z
                if num == 0:
                    len_zero += 1
            if num > 0:
                break
        k = len_num - 1
        if len_zero >= 3:
            result.append([0,0,0])
        while nums[k] > 0 :
            i = 0
            j = j1
            while i < j and nums[i] <= 0 and nums[j] <= 0:
                if nums[i] + nums[j] + nums[k] > 0:
                    j -= 1
                    while i < j:
                        if nums[j + 1] == nums[j]:
                            j -= 1
                        else:
                            break
                elif nums[i] + nums[j] + nums[k] < 0:
                    i += 1
                    while i < j:
                        if nums[i - 1] == nums[i]:
                            i += 1
                        else:
                            break
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    i += 1
                    j -= 1
                    while i < j and j >= 1 and i < len_num - 2 and nums[i] == nums[i - 1] and nums[j] == nums[j + 1]:
                        i += 1
                        j -= 1
            k -= 1
            while k >= 2 and nums[k] > 0 and nums[k] == nums[k+1]:
                k -= 1

        i1 = 1
        for z, num in enumerate(nums):
            if num > 0:
                i1 = z
                break
        k = 0
        while k < len_num-2 and nums[k] < 0:
            i = i1
            j = len(nums) - 1
            while i < j and nums[i] > 0 and nums[j] > 0:
                if nums[i] + nums[j] + nums[k] > 0:
                    j -= 1
                    while i < j:
                        if nums[j + 1] == nums[j]:
                            j -= 1
                        else:
                            break
                elif nums[i] + nums[j] + nums[k] < 0:
                    i += 1
                    while i < j:
                        if nums[i - 1] == nums[i]:
                            i += 1
                        else:
                            break
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    i += 1
                    j -= 1
                    while i < j and j >= 2 and i <= len_num - 2 and nums[i] == nums[i - 1] and nums[j] == nums[j + 1]:
                        i += 1
                        j -= 1
            k += 1
            while k < len_num - 2 and nums[k] == nums[k-1]:
                k += 1
        return result
    def threeSum(self, nums) :
        plusNumber = []
        negativeNumber = []
        zeroNumber = []
        resulNum = []
        for i in nums:
            if i > 0:
                plusNumber.append(i)
            elif i < 0:
                negativeNumber.append(i)
            elif i == 0:
                zeroNumber.append(0)
        if len(zeroNumber) >= 3:
            resulNum.append([0,0,0])
        plusNumber.extend(zeroNumber)
        for i,value_i in enumerate(plusNumber):
            for j in range(i+1, len(plusNumber)):
                for k in negativeNumber:
                    if value_i + plusNumber[j] + k == 0:
                        if value_i <= plusNumber[j] and [value_i, plusNumber[j], k] not in resulNum:
                            resulNum.append([value_i, plusNumber[j], k])
                            # resulNum.add(str(value_i)+str(plusNumber[j])+str(k))
                        elif value_i > plusNumber[j] and [plusNumber[j], value_i, k] not in resulNum:
                            resulNum.append([plusNumber[j], value_i, k])
                            # resulNum.add(str(plusNumber[j]) + str(value_i) + str(k))
        for i,value_i in enumerate(negativeNumber):
            for j in range(i+1, len(negativeNumber)):
                for k in plusNumber:
                    if value_i + negativeNumber[j] + k == 0:
                        if value_i <= negativeNumber[j] and [value_i, negativeNumber[j], k] not in resulNum:
                            # resulNum.add(str(value_i) + str(negativeNumber[j]) + str(k))
                            resulNum.append([value_i, negativeNumber[j], k])
                        elif value_i > negativeNumber[j] and [negativeNumber[j], value_i, k] not in resulNum:
                            # resulNum.add(str(negativeNumber[j]) + str(value_i[j]) + str(k))
                            resulNum.append([negativeNumber[j], value_i, k])
        return resulNum
S = Solution()
print(S.threeSum1([[-1,0,1,2,-1,-4]]))
