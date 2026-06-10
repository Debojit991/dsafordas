class Solution:
    def isPalindrome(self, n):
        temp=n
        s=0
        while(temp>0):
            d=temp%10
            s=s*10+d
            temp//=10
        if n==s:
            return True
        else:
            return False
