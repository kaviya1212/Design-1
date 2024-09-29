class Solution:
    #time complexity = o(n)
    #space complexity = o(n)
    # Two dictionaries are used to track character mappings between s and t.
    #for every letter in s/t check if the letter is present in map_s_to_t/map_t_to_s. 
    #If the characters are not mapped yet, they are added to the dictionaries as a new pair.
    # if its pressent check if the new key is same as the old.
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s_to_t = {}
        map_t_to_s = {}
        
        for i in range(len(s)):
            if s[i] in map_s_to_t:
                if map_s_to_t[s[i]] != t[i]:
                    print(map_s_to_t[s[i]], t[i])
                    return False
            else:
                map_s_to_t[s[i]] = t[i]

            if t[i] in map_t_to_s:
                if map_t_to_s[t[i]] != s[i]:
                    return False
            else:
                map_t_to_s[t[i]] = s[i]
        return True


