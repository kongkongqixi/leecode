class Solution:
    # def canTransform(self, start: str, end: str) -> bool
        def canTransform(self, start:str, end:str):
            if len(start) != len(end):
                return False
            s_r_sum = []
            s_l_sum = []
            r_l_sum = []

            x_sum = 0
            for i in start:
                if i == 'X':
                    x_sum += 1
                elif i =='R':
                    s_r_sum.append(x_sum)
                    r_l_sum.append('R')
                elif i =='L':
                    s_l_sum.append(x_sum)
                    r_l_sum.append('L')
            end_r_index = 0
            end_l_index = 0
            end_x_sum = 0
            end_l_r_index = 0
            for i in end:
                if i == 'X':
                    end_x_sum += 1
                elif i == 'R':
                    if end_l_r_index >= len(r_l_sum) or r_l_sum[end_l_r_index] != 'R':
                        return False
                    end_l_r_index += 1
                    if end_x_sum < s_r_sum[end_r_index]:
                        return False
                    else:
                        end_r_index += 1
                elif i == 'L':
                    if end_l_r_index >= len(r_l_sum) or r_l_sum[end_l_r_index] != 'L':
                        return False
                    end_l_r_index += 1
                    if end_x_sum > s_l_sum[end_l_index]:
                        return False
                    else:
                        end_l_index += 1
            if end_l_r_index < len(r_l_sum):
                return False
            return True


# "XLLR"
# "LXLX"
s= Solution()
print(s.canTran('XLLR', 'LXLX'))
