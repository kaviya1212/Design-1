from collections import Counter

class Solution:
    # time complexity: O(nlogn)
    # space complexity: O(n)
    # get the unique numbers and the count of each number in a dictionary. for every unique number calculate points by multiplying the number by its count.
    #It then iterates through the sorted unique numbers, updating two variables (prev_earn and curr_earn) to track the maximum points. while ignoring nums[i]+1 and nums[i]-1. 
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        unique_nums = sorted(count.keys())

        prev_earn = 0
        curr_earn = 0

        for i in range(len(unique_nums)):
            num = unique_nums[i]
            points = num * count[num]

            if i>0 and num == unique_nums[i-1]+1:
                new_earn = max(curr_earn, prev_earn + points)
            else:
                new_earn = curr_earn + points
            
            prev_earn = curr_earn
            curr_earn = new_earn

        return curr_earn
