#Given two strings s and t, return true if t is an anagram of s, and false otherwise.

#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

class Solution:
    def isAnagram(self , s: str ,t:str) -> bool:
        if len(s) != len(t):
            return False
        elif (sorted(s) == sorted(t)):
            return True
        else:
            return False


#test
s = "anagrama"      
t = "margana"  
print("Is Anagram : ",Solution().isAnagram(s=s,t=t))