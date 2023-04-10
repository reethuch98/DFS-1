# TC : O(m*n) 
# SC : O(N)
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        curr_color = image[sr][sc]
        R, C = len(image), len(image[0])
        if color==curr_color:
            return image
        def dfs(sr, sc):
            if image[sr][sc]==curr_color:
                image[sr][sc] = color
                if sr >=1: dfs(sr-1, sc)
                if sc >=1: dfs(sr, sc-1)
                if sr+1 < R : dfs(sr+1, sc)
                if sc + 1 <C: dfs(sr, sc+1)
        dfs(sr, sc)
        return image
            
        
