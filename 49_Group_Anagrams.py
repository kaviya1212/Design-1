from collections import defaultdict
#time complexity = O(n * m log m)
#space complexity = O(n * m)
#default dict is used to create a new list for each individual anagram. 
#The strings are sorted and added to a tuple and used as the key.
#With the sorted alphabets as key, strs are added to the list and then the values are printed.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagrams = defaultdict(list)
        result = []

        for s in strs:
            sorted_strs = tuple(sorted(s))
            group_anagrams[sorted_strs].append(s)
        
        for values in group_anagrams.values():
            result.append(values)

        return result
