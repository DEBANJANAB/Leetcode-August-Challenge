class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        array=Counter(nums)
        d=dict(array)
        for key in d:
            if d[key]==1:
                return key
        