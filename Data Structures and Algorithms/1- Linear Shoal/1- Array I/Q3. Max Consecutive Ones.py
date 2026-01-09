class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        temp_count = 0
        max_count = 0
        for num in nums :
            if num == 1 :
                temp_count += 1
            if(temp_count > max_count) :
                max_count = temp_count
            if num == 0:
                temp_count = 0
        return max_count
        
