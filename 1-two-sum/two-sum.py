class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num={}
        n=len(nums)
        for i in range(n):
            com=target-nums[i]
            if com in num:
                return [num[com],i]
            num[nums[i]]=i
        return []
            