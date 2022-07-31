# This section contains the imports for running the code
# math library is used in the dividing step 
import math

# Importing the Basic_Algorithm.py file to get the minimum penalty if length of string is less than 2 i.e Base Case 
import Basic_Algorithm 


# Function is used to calculate the minimum penalty for the efficient algorithm
def get_Minimum_Penalty_efficient(str_x, str_y, mismatch, gap_penalty):
    a = len(str_x)
    b = len(str_y)

    dp = [[0 for i in range(b+1)] for j in range(2)]
    
    # Creating a dictionary to map the Bases 
    chars = {
        'A' : 0,
        'C' : 1,
        'G' : 2,
        'T' : 3
    }
    # Calculating the values in the 'dp' matrix
        
    for i in range(b+1):
        dp[0][i] = i * gap_penalty

    dp[1][0] = gap_penalty
        
    for i in range(1, a+1):
        for j in range(1, b+1):
            if str_x[i-1] == str_y[j-1]:
                dp[1][j] = dp[0][j-1]
            else:
                x = str_x[i-1]
                y = str_y[j-1]
                dp[1][j] = min(dp[0][j-1] + mismatch[chars[x]][chars[y]], dp[0][j] + gap_penalty, dp[1][j-1] + gap_penalty)
        
        for k in range(b+1):
            dp[0][k] = dp[1][k]

        if i != a:
            dp[1][0] = dp[1][0] + gap_penalty 
    
    return dp[-1]

def divide_and_conquer(str_x, str_y, mismatch, gap_penalty):
    """
    The divide_and_conquer function follows a modified version of the divide and conquer from Algorithm Design - Eva Tardos
 
    Algorthim:
    
    Divide-and-Conquer-Alignment(a,b)
    Let m be the number of symbols in a
    Let n be the number of symbols in b
    If m ≤ 2 or n ≤ 2 then
    Compute optimal alignment using Alignment(a,b)
    Return Result
    Call Space-Efficient-Alignment(a[1 : n/2],b)
    Call Backward-Space-Efficient-Alignment(a[1 : n/2],b)
    Let q be the index minimizing f (q, n/2) + g(q, n/2)
    Divide-and-Conquer-Alignment(a[1 : q],b[1 : n/2])
    Divide-and-Conquer-Alignment(a[q + 1 : n],b[n/2+ 1 : n])
    Combine the returned result
    """


    # The following are the base cases:
    if len(str_x) <= 2 or len(str_y) <= 2:
        return Basic_Algorithm.get_Minimum_Penalty(str_x, str_y, mismatch, gap_penalty)

    # The following code divides a into 2 parts for finding the Q point
    x_mid = math.ceil(len(str_x)/2)
    # Getting the last columns of the DP array

    # This finds the costs from the left bottom to all the points in the divided row
    y_left = get_Minimum_Penalty_efficient(str_x[:x_mid], str_y, mismatch, gap_penalty)
    # This finds the costs from the right top corner to all the points the divided row
    y_right = get_Minimum_Penalty_efficient(str_x[x_mid:][::-1], str_y[::-1], mismatch, gap_penalty)

    idx = 0
    y_mid = -1
    min_cost = float("inf")
    for a, b in zip(y_left, y_right[::-1]):
        # Updates the y_mid and min_cost
        if min_cost > (a + b):
            y_mid = idx
            min_cost = a+b
        idx += 1

    lx, ly, lc = divide_and_conquer(str_x[:x_mid], str_y[:y_mid], mismatch, gap_penalty)
    rx, ry, rc = divide_and_conquer(str_x[x_mid:], str_y[y_mid:], mismatch, gap_penalty)

    return lx+rx, ly+ry, lc+rc
