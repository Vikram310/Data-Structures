def pascal(numRows):

    '''
        Link: https://leetcode.com/problems/pascals-triangle/
        Intuition:
            Pascal Triangle is direct sum of elements above each element in each row. However the issues arises only for the corner elements in each row. 
            Also, corner elements are always same i.e., 1 
        Approach:
            First and last element of each row is always 1, so we have 2 approaches
                Approach - 1: Initialize the first and last element of each row as 1 before inserting the rows. 
                Approach - 2: As they are same, how about we append the previous row with [0] before and after, so that we can add just 0 and the elements and this new list can be a temporary .
        Time Complexity:
            As we are iterating over numRows almost twice - one for initial loop and other while creating each row, the Time Complexity will be O(n^2)
    '''
    res = [[1]]

    for i in range(numRows - 1):
        temp = [0] + res[-1] + [0]
        next = []
        for j in range(len(res[-1]) + 1):
            next.append(temp[j] + temp[j+1])
        res.append(next)
    return res