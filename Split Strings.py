def solution(s):
    ns = [i for i in s]
    if len(ns) % 2 == 1:
        ns.append("_")
    return [ns[i]+ns[i+1] for i in range(0,len(s),2)]
    

import re
def solution(s):
    return re.findall(".{2}", s + "_")

