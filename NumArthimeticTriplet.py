class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        num_set= set(nums)
        count=0
        for num in nums:
            if (num+diff in num_set) and (num+2*diff in num_set):
                count+=1
          
        return count
        
    