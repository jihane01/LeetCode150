# Approach 
# i have strings array i have to search anagrams words 
# order the words alphabetlic  
#i add them to a hash table the sorted every element alphabitcally 
# compare element li equals and print them 

class Solution:
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        
        return list(anagram_map.values())
    
      