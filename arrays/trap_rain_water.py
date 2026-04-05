class Solution:
    def maxWater(self, arr):
        self.arr=arr
        total_water=0
        left_max=0
        right_max=0
        l,r=0,len(arr)-1
        
        while(l<=r):
            
            if (arr[l]<=arr[r]): # left is smaller than right
                
                if(left_max<arr[l]):
                    left_max=arr[l]
                else:
                    total_water+= left_max-arr[l]
                l+=1
                
                
            else: # right is smaller than left
            
                if (arr[r]>=right_max):
                    right_max=arr[r]
                else:
                    total_water+= right_max -arr[r]
                r-=1
        return total_water