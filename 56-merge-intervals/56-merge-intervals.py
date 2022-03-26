# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         for i in intervals:
#             for j in i
#             if i[1] >= i+1[0]:
#                 i[0]=i[0]
#                 i[1]=i+1[1]
#         return inetrvals
        
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals = sorted(intervals)
        for inter in intervals:
            if res and inter[0]<=res[-1][1]:
                res[-1][1] = max(res[-1][1], inter[1])
            else:
                res += [inter]
        return res
    