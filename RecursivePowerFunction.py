#Dhruv Govil Period 2 March 8 2016
#Recursive Power Function Program

def power(base, exponent): 
        '''Calculates base to the power exponent'''
	#Terminating Cases 
        if exponent == 0:
                return 1 
 	#Recursive Call 
        return base * power(base, exponent - 1)                

        
    



    

