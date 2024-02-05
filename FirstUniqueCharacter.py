class Solution:
    def firstUniqChar(self, s: str) -> int:
        frequency = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for j in range (len(s)):
            frequency[ord(s[j])-ord('a')] += 1

        for j in range (len(s)):
            if (frequency[ord(s[j])-ord('a')] == 1):
                return j;
        
        return -1;
