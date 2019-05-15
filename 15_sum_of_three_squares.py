class Solution:
    def a(self, nums):
        plus = []
        neg = []
        zero_len = 0
        num_dict = {}
        result = []
        for i in nums:
            if i in num_dict.keys():
                num_dict[i] += 1
            else:
                num_dict[i] = 1

            if i > 0 and i not in plus:
                plus.append(i)
            elif i < 0 and i not in neg:
                neg.append(i)
            elif i == 0:
                zero_len += 1

        if len(neg) == 0:
            if zero_len < 3:
                return []
            else:
                return [[0, 0, 0]]

        if len(plus) == 0:
            if zero_len < 3:
                return []
            else:
                return [[0, 0, 0]]

        neg.sort()
        plus.sort()
        if zero_len >= 3:
            result.append([[0,0,0]])
        for n in neg:
            if (0-n/2 in plus) and (num_dict[0-n/2] >1):
                result.append([n,int(0-n/2), int(0-n/2)])
            for p in plus:
                val = 0 - n - p
                if val > 0:
                    if val <= p:
                        continue
                    if val in plus:
                        result.append([val, p, n])
                elif val < 0 :
                    if val < n:
                        break
                    elif val == n and num_dict[n] > 1:
                        if val in neg:
                            result.append([n, val, p])
                    elif val >n and val in neg:
                        result.append([n, val, p])

                elif val == 0:
                    if zero_len > 0:
                        result.append([n, p, 0])
        return result




    def threeSum2(self, nums):
        nums.sort()
        result = []
        len_num = len(nums)

        if len_num < 3 or nums[0] > 0 or nums[len_num - 1] < 0:
            return []

        if nums[0] == nums[len_num - 1] == 0:
            return [[0, 0, 0]]

        if (nums[0] == 0 and nums[2] == 0) or (nums[len_num - 3] == 0 and nums[len_num - 1] == 0):
            return [[0, 0, 0]]

        len_zero = 0
        for num in nums:
            if num == 0:
                len_zero += 1
            if num > 0:
                break
        k = len_num - 1
        if len_zero >= 3:
            result.append([0, 0, 0])

        while nums[k] > 0:
            i = 0
            j = k - 1
            while i < j and nums[i] <= 0:
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
            while k >= 2 and nums[k] > 0 and nums[k] == nums[k + 1]:
                k -= 1
        return result
S = Solution()
print(S.a([[-1,0,1,2,-1,-4]]))
