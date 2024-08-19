
class Solution(object):
    def gcd(self,a ,b):
        while b:
            a,b= b, a % b
        return a
    def smallestEvenMultiple(self,n ):
        gcd = self.gcd(2, n)
        lcm = (2 * n )// gcd
        return lcm
        