class Solution:
    def countDigit(self, n):
        temp=n
        c=0
        while(temp>0):
            c+=1
            temp=temp//10
    
        return c