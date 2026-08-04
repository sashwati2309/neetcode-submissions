class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strmap = {}
        for i in range(len(strs)):
            s = "".join(sorted(strs[i]))
            if strmap.get(s) is None:
                w= []
                w.append(strs[i])
                strmap[s]=w
            else:
                strmap[s].append(strs[i])
            
        res = []
        for i in strmap:
            res.append(strmap.get(i))
        return res
