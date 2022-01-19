'''''
Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
'''''

#Function
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        sep_jewels = list(jewels)
        sep_stones = list(stones)
        for i in stones:
            for j in jewels:
                if i == j:
                    count = count +1
                    
        return count
                


