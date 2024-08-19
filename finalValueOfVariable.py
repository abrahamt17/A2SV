class Solution(object):
    def finalValueAfterOperations(self, operations):
        # Initialize X
        X = 0
        
        # Process each OPERATION
        for OPERATION in operations:
            if OPERATION == "++X" or OPERATION == "X++":
                X += 1
            elif OPERATION == "--X" or OPERATION == "X--":
                X -= 1
        
        return X

