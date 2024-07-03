class Solution(object):
    def __init__(self):
        self.memo = {}
    def tribonacci(self, n):
        if n in self.memo:
            return self.memo[n]
        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        #Memoization as part of dynamix programmping to be faster
        result=self.tribonacci(n-3)+self.tribonacci(n-1)+self.tribonacci(n-2)
        self.memo[n] = result
        return result