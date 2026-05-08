class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h,e={},{}
        for i in s:
            if(i in h):
                h[i]=h[i]+1
            else:
                h[i]=1
        for j in t:
            if(j in e):
                e[j]=e[j]+1
            else:
                e[j]=1
        return h==e