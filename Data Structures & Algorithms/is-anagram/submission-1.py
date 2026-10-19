class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        dict_s = {}
        dict_t = {}

        for l in s:
            dict_s[l] = dict_s.get(l, 0) + 1

        
        for char in t:
            dict_t[char] = dict_t.get(char, 0) + 1

        return dict_s == dict_t



    