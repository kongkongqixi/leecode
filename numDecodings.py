class Solution:
    def numDecodings(self, s):
        if len(s) == 0:
            return 0
        if len(s) == 1:
            if s == '0':
                return 0
            return 1
        if s[0] == '0':
            return 0
        s_1 = 1
        s_2 = 0
        if s[1] == '0' and (s[0] == '0' or int(s[0]) > 2):
            return 0
        if s[1] == '0':
            s_2 = 1
        elif 10 < int(s[0:2]) < 27:
            s_2 = 2
        else:
            s_2 = 1
        for i in range(3, len(s)+1):
            if s[i-1] == '0':
                if s[i-2] == '0' or int(s[i-2]) > 2:
                    return 0
                else:
                    temp = s_1
                    s_1 = s_2
                    s_2 = temp
            else:
                if s[i-2] == '0':
                    s_1 = s_2
                else:
                    if 9 < int(s[i-2:i]) < 27:
                        temp = s_1 + s_2
                        s_1 = s_2
                        s_2 = temp
                    else:
                        s_1 = s_2
        return s_2
s = Solution()
print(s.numDe('227'))
