'''''
Example 1:
Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
'''''

#Function
class Solution:
    def defangIPaddr(self, address: str) -> str:
        new_address = list(address)
        for i in range(len(new_address)):
            if new_address[i] == ".":
                new_address[i] = "[.]"
                address = "".join(new_address)
        
        
        
        return address