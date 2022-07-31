# If we want to take File Input from the user
# echo "Enter the file name of the input file or Drag and Drop the file:"

# read f_name

# # Check if the file exists 
# if [ -f "$f_name" ]; then

#     echo "File:" $f_name "exists.\n"
#     echo "--------------------------------"
 

#     python3 9190064859_2792744306_basic.py --file $f_name
    
#     printf "\nOutput stored in the output.txt file"


# else
# 	# File Not Found
# 	echo "File: " $f_name "Not Found. Please Try Again"

# 	# Rerun the script if file is not found 
# 	./basic.sh
# fi


python3 9190064859_2792744306_basic.py input.txt

printf "\nOutput stored in the output.txt file"
