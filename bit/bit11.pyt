class Solution:
	def AllPossibleStrings(self, s):
	    li=[]
	    n=len(s)
        for i in range(2**n):
            ans=""
            for j in range(len(s)):
                if (i&1):
                    ans+=(s[j])
                    i=i>>1
                else:
                    i=i>>1
                    continue
                
            li.append(ans)    
        return sorted(li)