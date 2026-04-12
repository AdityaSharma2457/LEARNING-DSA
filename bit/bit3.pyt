def setBits(self, n):
	count=0
	self.n=n
	while(n):
		if n&1:
		    count+=1
		n=n>>1
	return count