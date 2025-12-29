def isAnagram(self, s: str, t: str) -> bool:
    from collections import defaultdict
    str1 = defaultdict(int)
    str2 = defaultdict(int)

    for x in s:
        str1[x] +=1
    for x in t:
        str2[x]+=1

    return str1==str2