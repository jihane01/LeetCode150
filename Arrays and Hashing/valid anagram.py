''' we have t and s variables '''
''' compare t and s '''
def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
            return False
    elif sorted(s) == sorted(t):
            return True
    else:
            return False


