#User function Template for python3

class Solution:
    def findPosition(self, n):
        if ( n>0 and n&(n-1)==0):
            return ((n&(-n)).bit_length())
        else:
            return -1