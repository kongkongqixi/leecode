class Solution:
    def hIndex(self, citations) -> int:
        if len(citations) == 0:
            return 0
        citations.sort()
        h = len(citations) - 1
        paper_num = 0
        reference = 0
        while h >= 0:
            paper_num += 1
            reference = citations[h]
            if paper_num < reference:
                h -= 1
                continue
            elif paper_num == reference:
                return reference
            else:
                return paper_num - 1
        return paper_num

s = Solution()
print(s.hIndex([4,0,6,1,5]))

