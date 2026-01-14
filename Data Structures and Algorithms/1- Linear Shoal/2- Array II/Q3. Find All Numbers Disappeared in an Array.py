class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set(nums)
        n = len(nums)
        ans = []
        for num in range(1, n+1) :
            if num not in s :
                ans.append(num)

        return ans

        
