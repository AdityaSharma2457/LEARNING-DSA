#User function Template for python3

class Solution:
    def setSetBit(self, x, y, l, r):
        mask=0
        for i in range(l-1,r):
            mask|= 2**i
            
        copied_bits=y&mask
        
        return x|copied_bits