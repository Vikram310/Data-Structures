class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Link to the problem : https://leetcode.com/problems/next-permutation/description/
        Intuition:
            Next permutation is just swapping the correct numbers like next permutation of [1,2,3] is [1,3,2]. Here, we can see that numbers 2,3 are just swapped and 1 is not changed.
        Approach:
            Start from right/end of list, check if there is any pattern of descending order and find the breakpoint where the order is stopped.
            Once we find the breakpoint, just iterate from end to that point and swap the numbers.
            If the breakpoint is not found, then the list is in descending order andwe have to return the reverse of it. Once we find the breakpoint, just iterate from end to that point and swap the numbers.
        
        """
        
        # If the length of list is less than 3, then next permutation will be reverse of this number 
        if len(nums) < 3:
            return nums.reverse()

        # set a pointer at last -1 position to start comparing the values
        pointer = len(nums) - 2 # 2 because indexing starts from 0

        #find the position where descending pattern is stopped. 
        while pointer >=0 and nums[pointer] >= nums[pointer+1]:
            pointer -= 1 
        
        if pointer == -1: #the list is in descending order
            return nums.reverse()
        
        # now we found the position where the descending pattern is stopped, so we will swap those variables
        for x in range(len(nums)-1, pointer,-1):
            if nums[pointer] < nums[x]:
                nums[pointer],nums[x] = nums[x],nums[pointer]
                break
        
        nums[pointer+1:] = reversed(nums[pointer+1:])