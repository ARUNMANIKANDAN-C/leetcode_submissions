class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        ans=[]
        dep = 0
        for i in seq:
            if i ==")":
                dep-=1
            ans.append(dep%2)
            if i =="(":
                dep+=1
        return ans
