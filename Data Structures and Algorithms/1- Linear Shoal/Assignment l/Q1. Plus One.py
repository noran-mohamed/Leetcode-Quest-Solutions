class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        char = ''
        for i in range(len(digits)) :
            char += str(digits[i])
        num = int(char)
        num += 1 
        ans = []

        for n in str(num) :
            ans.append(int(n))
        return ans
        
        
