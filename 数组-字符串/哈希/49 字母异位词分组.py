from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key in cache:
                cache[key].append(s)
            else:
                cache[key] = [s]
        return list(cache.values())
    
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        cache = {}
        for item in strs:
            k = ''.join(sorted(item))
            if k in cache:
                cache[k].append(item)
            else:
                cache[k] = [item]
        return list(cache.values())
