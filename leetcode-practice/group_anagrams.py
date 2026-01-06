from typing import List


strs1 = ["act","pots","tops","cat","stop","hat"]

strs1_ans=[["hat"],["act", "cat"],["stop", "pots", "tops"]]

strs2 = ["act","pots","tops","cat","stop","hat"]

str2_ans=[["hat"],["act", "cat"],["stop", "pots", "tops"]]

strs3 = [""]

strs3_ans=[[""]]
from collections import defaultdict
defdict = defaultdict(list)
def groupAnagrams(strs: List[str]):
    for x in strs:
        l = [0]*26
        for char in x:
            l[ord(char)-97] +=1
        tup = tuple(l)
        defdict[tup].append(x)
        return list(defdict)
        
        
