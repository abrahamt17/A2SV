class Solution(object):
    def numIdenticalPairs(self, nums):
        # Dictionary to count occurrences of each number
        count_map = {}
        
        # Count the occurrences
        for num in nums:
            if num in count_map:
                count_map[num] += 1
            else:
                count_map[num] = 1
        
        # Calculate the number of good pairs
        good_pairs = 0
        for count in count_map.values():
            if count > 1:
                good_pairs += count * (count - 1) // 2
        
        return good_pairs



sol = Solution()
print("NUMBER1" , sol.numIdenticalPairs([1,2,3,1,1,3]))  # Output: 4
print("NUMBER2" , sol.numIdenticalPairs([1,1,1,1]))      # Output: 6
print("NUMBER3" ,  sol.numIdenticalPairs([1,2,3]))        # Output: 0
