class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        myHash = defaultdict(int)
        myHash2 = defaultdict(int)
        for x in s:
            myHash[x] += 1
        for x in t:
            myHash2[x] += 1
        
        return myHash == myHash2