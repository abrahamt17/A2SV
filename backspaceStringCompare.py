class Solution(object):
    def backspaceCompare(self, s, t):
        def building_string(st):
            stack=[]
            for char in st:
                if char!="#" and stack:
                    stack.append(char)
                    
                elif stack:
                    stack.pop()
            return ''.join(stack)
        return building_string(s) == building_string(t)
sol = Solution()
print(sol.backspaceCompare("ab#c", "ad#c"))  
print(sol.backspaceCompare("ab##", "c#d#"))  
print(sol.backspaceCompare("a#c", "b"))
        
    
                
            
                
        
                

    
       