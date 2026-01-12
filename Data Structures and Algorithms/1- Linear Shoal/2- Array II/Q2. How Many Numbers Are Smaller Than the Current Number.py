class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            tot = 0
            for i in range(0, len(nums)):
                if nums[i] < num :
                    tot += 1
            ans.append(tot)
        return ans
        
