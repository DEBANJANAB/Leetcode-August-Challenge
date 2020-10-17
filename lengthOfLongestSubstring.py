# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def check(s):
            for i in range(len(s)):
                for j in range(i + 1,len(s)): 
                    if(s[i] == s[j]):
                        return False;
            return True;
        if len(s) == 0 or len(s) == 1:
            return len(s)
        else:
            subs = [s[i: j] for i in range(len(s)) 
              for j in range(i + 1, len(s) + 1)]
            
            m = len(subs[0])
            for sub in subs:
                if check(sub):
                    if len(sub) > m:
                        m = len(sub)
            return m
        