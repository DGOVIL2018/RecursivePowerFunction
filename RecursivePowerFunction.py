#Dhruv Govil Period 2 March 8 2016
#Recursive Power Function Program

def power(base, exponent): 
	
	#Terminating Cases 
 	if exponent == 0: 
 		return 1 
 	#Recursive Call 
 	return base * power(base, exponent - 1) 
	 
#####MAIN PROGRAM BEGINS HERE#####
    #test whether inputs are valid integers
    


b = (input("Enter an integer base: "))
e = (input("Enter a non-negative integer exponent: "))
b = int(b)
e = int(e)

if (b % 1 == 0) and (e % 1 == 0) and (e >= 0) and (b != 0 or e != 0):

    result = power(b,e)
    if result == False:
        print("Please enter an integer base and a non-negative integer exponent")
    else:
        print(result)
    
       

    

