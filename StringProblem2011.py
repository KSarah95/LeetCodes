'''''
Example 1:

Input: operations = ["--X","X++","X++"]
Output: 1
Explanation: The operations are performed as follows:
Initially, X = 0.
--X: X is decremented by 1, X =  0 - 1 = -1.
X++: X is incremented by 1, X = -1 + 1 =  0.
X++: X is incremented by 1, X =  0 + 1 =  1.
'''''

#Function
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x=0
        for i in operations:
            if i == "--X":
                x = x-1
            if i == "X--":
                x = x-1
            if i == "++X":
                x = x+1
            if i == "X++":
                x = x+1
        
        return x


