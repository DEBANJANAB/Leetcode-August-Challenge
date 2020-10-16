class Solution:
    def partition(self, s: str) -> List[List[str]]:
        part = [[] for _ in range(len(s))]
        def sub_part(l, r):
            if 0 <= l <= r < len(s) and s[l]==s[r]:
                part[l].append(s[l:r+1])
                sub_part(l-1, r+1)
                
		# find all palindromes
        for i in range(len(s)):
            sub_part(i,i)
            sub_part(i-1,i)
			
        # generate output
		res=[]
		
        def dfs(i, tmp):
            if i >=len(s):
                res.append(tmp)
			else:
				for p in part[i]:
					dfs(i + len(p), tmp + [p])        
        
		dfs(0, [])
        return res