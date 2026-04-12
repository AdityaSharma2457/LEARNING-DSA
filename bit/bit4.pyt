
class Solution:
	def singleNum(self, arr):
		xor_all=0
		for item in arr:
		    xor_all^=item
			
	    last_bit_of_xor_all=xor_all&(-xor_all)
		xor1=0
		xor2=0
		for item in  arr:
		    if last_bit_of_xor_all & item:
		        xor1^=item
		    else:
		        xor2^=item
		return sorted([xor1,xor2])