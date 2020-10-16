def numDistinct(self, s: str, t: str) -> int:
        if not t:
            return 1
        if len(s) < len(t):
            return 0
        seen_so_far = {i:0 for i in range(len(t))}
        for c in s:
            for i in reversed(range(len(t))):
                if t[i] == c:
                    seen_so_far[i] += seen_so_far[i-1] if i > 0 else 1
        return seen_so_far[len(t) - 1]