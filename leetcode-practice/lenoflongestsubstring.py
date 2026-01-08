s="dvdf"
def lenoflongestsubstring(s):
    if not len(s):
        return 0
    max_res = 1
    hash_set = set()
    l = 0
    r = 1

    hash_set.add(s[l])
    while r < len(s):
        old_len = len(hash_set)
        hash_set.add(s[r])
        if len(hash_set) == old_len:
            hash_set.remove(s[l])
            l+=1
        else:
            r+=1
            max_res = max(max_res, len(hash_set))
    return max_res