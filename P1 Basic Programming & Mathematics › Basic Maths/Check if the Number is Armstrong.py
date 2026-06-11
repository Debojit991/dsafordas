class Solution:
  def isArmstrong(self,n):
    num=n
    sum=0
    while num>0:
      digits = [int(d) for d in str(num)]
      i=len(digits)
      for d in digits:
        d=num%10
        sum=sum+d**i
        num//=10
    if sum == n:
       return True
    else:
        return False
