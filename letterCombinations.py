class Solution:
    def letterCombinations(self, digits):
        temp_dict = dict()
        temp_dict['2'] = 'abc'
        temp_dict['3'] = 'def'
        temp_dict['4'] = 'ghi'
        temp_dict['5'] = 'jkl'
        temp_dict['6'] = 'mno'
        temp_dict['7'] = 'pqrs'
        temp_dict['8'] = 'tuv'
        temp_dict['9'] = 'wxyz'
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return [i for i in temp_dict[digits]]
        result = [i for i in temp_dict[digits[0]]]
        for i in range(1, len(digits)):
            result = self._a(result, temp_dict[digits[i]])
        return result


    def _a(self, str_re, str_add):
        total = []
        for i in str_add:
            for j in str_re:
                total.append(j+i)
        return total
S = Solution()
print(S.letterCombinations('34'))

