# How to calculate standard Deviation with python
# code written by Adeyemi Oluwaseyi 


#import math library to enable the use of square root
import math

'''create an input function 
that collects the user data values in 
string separated by space

Also split the space with a comma
'''


input_list = input("Enter the elements of the list separated by space below '\n: ")
print("\n")
#split the data with a comma instead of the space
user_list = input_list.split()



#using a for loop to iterate over the list
for i in range(len(user_list)):
    
    # convert the elements in the list to an integer
    user_list[i] = int(user_list[i])

#We then assign the list in integer to variable x 
# so that it can fit into the functions
x = user_list 

#### FUNCTION FOR CALCULATING MEAN DEVIATION ####
def find_mean(x):
    # print out the total sum of the element in list
    # divided by the number of element in the list
    return f'The mean is: {sum(x)/ len(x)}'

#print out the mean result
print(find_mean(x))

### FUNCTION FOR STANDARD DEVIATION ###
def standard_d(x):
    #Calculate the mean of list assign to variable meen
    meen = sum(x)/ len(x)
    #loop through the list by subtracting the mean diviation from each element
    meand = [s-meen for s in x]
    # loop through the list by squaring each element in the list
    meand = [q**2 for q in meand]
    # return the square root of the sum of all the element in the list
    # divide by the number of element in the list subtracted by 1
    return math.sqrt(sum(meand)/(len(x)-1))

# print out the standard deviation
print(f"The standard Deviation is: {standard_d(x)}")
print('\n')
