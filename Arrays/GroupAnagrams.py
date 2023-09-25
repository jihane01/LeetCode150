# Approach 
# i have strings array i have to search anagrams words 
# order the words alphabetlic  
#i add them to a hash table the sorted every element alphabitcally 
# compare element li equals and print them 


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=collections.defaultdict(list)
        [d[''.join(sorted(i))].append(i) for i in strs]
        return d.values()