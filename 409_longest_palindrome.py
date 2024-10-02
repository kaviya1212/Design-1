class Solution:
    # time complexity O(n)
    # space complexity O(1) - 52 unique letters
    # calculate the number of times a letter occurs in s and store it in a dictionary. The count of letters is divided by 2 and multipled by 2 to add even number of letters to create apalindrome.
    # if odd number of letters exsist one is added to the count as one letter can be used in the center
    def longestPalindrome(self, s: str) -> int:
        letter_count = {}
        count = 0
        has_odd = False  

        for char in s:
            if char not in letter_count:
                letter_count[char] = 1
            else:
                letter_count[char] += 1

        for count_value in letter_count.values():
            count += count_value // 2 * 2  
            if count_value % 2 == 1:
                has_odd = True  

        if has_odd:
            count += 1

        return count
            
