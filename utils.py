# Function to generate the Strings based on the given input file
def String_Generator(fp):
    # Read the file to generate X and Y strings. Split the file_lines by the newline character
    file_lines = open(fp, 'r').read().split('\n')
    X_string = file_lines[0]
    breakpt = 0
    Y_string = ''
    
    # Generating input string: X 
    for a in range(1, len(file_lines)):
        if file_lines[a].isdigit():
            temp_str1 = X_string[:int(file_lines[a])+1] + X_string + X_string[int(file_lines[a])+1:]
            X_string = temp_str1
        # if value is not a digit then we found the breakpoint
        else:
            breakpt = a
            Y_string = file_lines[breakpt]
            break
    
    # Generating the input string: Y, starting from the breakpt+1 index
    for b in range(breakpt+1, len(file_lines)):
        temp_str2 = Y_string[:int(file_lines[b])+1] + Y_string + Y_string[int(file_lines[b])+1:]
        Y_string = temp_str2

    #print(X_string, Y_string)
    return X_string, Y_string