def maxSubArray(nums):
    '''
    Approach - 1:
        Find all the possible subarrays and calculate their sum and then return the maximum sum of the subarrays.
        For this we need to traverse the entire list for 3 times - one for start index, one for end index and one for calculating the sum.
        As we have 3 traversals, the time complexity of this approach will be O(N^3)
    Approach - 2:
        One optimization to the above approach is to combine the second and third traversal, by saving the sum of one subarray and then just add the next new element.
        With this, we can find the sum in secodn iteration and avoid last traversal. 
        As we have 2 traversals, the time complexity of this approach will be O(N^2)
    Approach - 3:
        Main Idea: Remove Negative prefix
        While traversing, we remove the previously visited values if they are small than the new one, ignore the previous values/prefix 
        Apart from above, we will make the negative values to 0 while traversing
        We have only 1 traversal, the time complexity is O(N)
    '''
    maxSum = nums[0]
    curSum = 0
    
    for n in nums:
        if curSum <0 :
            curSum = 0
        curSum += n
        maxSum = max(maxSum,curSum)
    
    return maxSum


