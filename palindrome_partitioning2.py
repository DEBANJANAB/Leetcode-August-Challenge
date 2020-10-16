def minCut(self, s: str) -> int:
        mem = {}
        return self.helper(mem, s)
    
    def helper(self, mem, s):
        
        if self.isPal(s):
            return 0
        
        if s in mem:
            return mem[s]
        
        res = len(s) - 1
        for i in range(0, len(s)):
            cur = s[:i+1]
            if self.isPal(cur):
                if not self.helper(mem, s[i+1:]):
                    mem[s[i+1:]] = 0
                if i == len(s) - 1:
                    res = min(res, self.helper(mem, s[i+1:]))
                else:              
                    res = min(res, self.helper(mem, s[i+1:]) + 1)
                
        mem[s] = res
        return res
    
    def isPal(self, s):
        return  s == s[::-1]