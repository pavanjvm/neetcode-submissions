class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res =  defaultdict(list)

        for s in strs:
            counteds = ''.join(sorted(s))
            res[counteds] = res.get(counteds,[])
            res[counteds].append(s)
        return list(res.values())
        

