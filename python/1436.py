class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        myHash = {}
        for x in paths:
            myHash[x[0]] = x[1]
            
        for x in paths:
            if x[1] not in myHash:
                return x[1]
            
        return paths[-1][1]