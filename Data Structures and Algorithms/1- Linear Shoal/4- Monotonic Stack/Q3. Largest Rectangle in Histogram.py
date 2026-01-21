class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        max_Area = 0

        for i in range(n+1) :
            if i == n :
                cur_h = 0
            else :
                cur_h = heights[i]
            
            while stack and cur_h < heights[stack[-1]] :
                h = heights[stack.pop()]
                if not stack:
                    width = i 
                else:
                    width = i - stack[-1] - 1
                
                area = width*h
                max_Area = max(area, max_Area)
            
            stack.append(i)
        return max_Area
         
