class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h={}
        x=0
        for i in nums:
            if(i in h):
                return True
            else:
                h[i]=x
            x=x+1
        return False