class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)
        for i in strs:
            sorteds = "".join(sorted(i))
            val = count.get(sorteds,[])
            val.append(i)
            count[sorteds] = val
            
        return(list(count.values()))






        