class Solution:
    def countSetBits(self,n):
        i=0
        count=0
        
        while (1<<i) <=n:
            cycle_length=1<<(i+1)
            no_of_cycles=n//cycle_length
            count+=(1<<i)*no_of_cycles 
            
            remainder=n % cycle_length
            extras=max(0,remainder-(1<<i)+1)
            
            count+=extras
            i+=1
        return count
            