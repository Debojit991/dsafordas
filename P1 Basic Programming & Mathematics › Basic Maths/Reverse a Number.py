class Solution:
    def reverseNumber(self, n):
        temp=n
        s=0
        while(temp>0):
            d=temp%10
            s=s*10+d
            temp//=10
        return s
