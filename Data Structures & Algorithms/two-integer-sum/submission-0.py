class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h={}
        ans=[]
        x=0
        for i in nums:
            if(target-i in h):
                ans=[h[target-i],x]
                return ans 
            else:
                h[i]=x
            x=x+1
