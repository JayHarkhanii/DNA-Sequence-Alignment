# Function to get the Minimum Penalty/Cost of Sequence Alignment
def get_Minimum_Penalty(str_x, str_y, mismatch, gap_penalty):
    a = len(str_x)
    b = len(str_y)

    # Initializing the DP Matrix as 0 for all elements
    dp = [[0 for i in range(b+1)] for j in range(a+1)]
    
    # Creating a dictionary to map the Bases 
    chars = {
        'A' : 0,
        'C' : 1,
        'G' : 2,
        'T' : 3
    }
    # Initializing the values of the first column in the DP Matrix by their respective index * gap penalty(delta)
    for i in range(a+1):
        dp[i][0] = i * gap_penalty

    # Initializing the values of the first row in the DP Matrix by their respective index * gap penalty(delta)    
    for i in range(b+1):
        dp[0][i] = i * gap_penalty
        
    for i in range(1, a+1):
        for j in range(1, b+1):
            # If the characters match
            if str_x[i-1] == str_y[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                # Else if they don't match then take minimum of the 3 neighbours in the DP matrix after adding corresponding alpha or delta values
                x = str_x[i-1]
                y = str_y[j-1]
                dp[i][j] = min(dp[i-1][j-1] + mismatch[chars[x]][chars[y]], dp[i-1][j] + gap_penalty, dp[i][j-1] + gap_penalty)
            
    
    # Build Solution from the DP Matrix
    c = a + b
    i = a
    j = b
    pos_x, pos_y = c,c
    ans_x = [0 for e in range(c+1)]
    ans_y = [0 for f in range(c+1)]
    
    # While both string not equal to 0
    while (not(i == 0 or j == 0)): 
        # If character in X string and Y string match
        if str_x[i-1] == str_y[j-1]:
            ans_x[pos_x] = ord(str_x[i-1])
            ans_y[pos_y] = ord(str_y[j-1])
            i -= 1
            j -= 1
            pos_x -= 1
            pos_y -= 1
        
        # Else if there is mismatch in the X string and Y string character then we have 3 options: 
        # i. the value in the previous diagonal + corresponding mismatch cost(alpha)
        # ii. the value in the previous row + gap penalty(delta)
        # iii. the value in the previous column + gap penalty(delta)

        # i
        elif dp[i-1][j-1] + mismatch[chars[str_x[i-1]]][chars[str_y[j-1]]] == dp[i][j]:
            ans_x[pos_x] = ord(str_x[i-1])
            ans_y[pos_y] = ord(str_y[j-1])
            i -= 1
            j -= 1
            pos_x -= 1
            pos_y -= 1
        
        # ii
        elif dp[i-1][j] + gap_penalty == dp[i][j]:
            ans_x[pos_x] = ord(str_x[i-1])
            ans_y[pos_y] = ord("_")
            pos_x -= 1
            pos_y -= 1
            i -= 1
         
        # iii   
        elif dp[i][j-1] + gap_penalty == dp[i][j]:
            ans_x[pos_x] = ord("_")
            ans_y[pos_y] = ord(str_y[j-1])
            pos_x -= 1
            pos_y -= 1
            j -= 1
    
    # While length of X string is not 0
    while pos_x > 0:
        if i > 0:
            i -= 1
            ans_x[pos_x] = ord(str_x[i])
            pos_x -= 1
        
        else:
            ans_x[pos_x] = ord('_')
            pos_x -= 1
    
    # While length of Y string is not 0
    while pos_y > 0:
        if j > 0:
            j -= 1
            ans_y[pos_y] = ord(str_y[j])
            pos_y -= 1
        
        else:
            ans_y[pos_y] = ord('_')
            pos_y -= 1
    
    # Removing the extra gaps from the start of ans_x and ans_y
    start = 1
    for i in range(c, 0, -1):
        if chr(ans_y[i]) == '_' and chr(ans_x[i]) == '_':
            start = i + 1
            break

    X = ''
    Y = ''
    # Adding the Final Aligned Sequence to X
    for i in range(start, c+1):
        X += chr(ans_x[i])
    
    # Adding the Final Aligned Sequence to Y    
    for i in range(start, c+1):
        Y += chr(ans_y[i])
    
    #print(X,Y)
    return X, Y, dp[-1][-1] 
