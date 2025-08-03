#def functions for robust division calculator


#try:
    #def safe_divide(numerator, denominator):
        #esult = numerator / denominator
    
        #if denominator == 0:
            #raise ZeroDivisionError
        #else:
            #return result
#except ZeroDivisionError:
        #print("you cannot divide by zero")

    #except ValueError:
        #if numerator or denominator == "str":
            #raise ValueError
        #else:
            #return result
    
        #print("invalid input")

# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        # Attempt to convert inputs to float
        num = float(numerator)
        den = float(denominator)
        
        # Attempt the division
        result = num / den
        return f"The result of the division is {result:.1f}"
    
    except ZeroDivisionError:
        return("Error: Cannot divide by zero.") 
    
    except ValueError:
        return("Error: Please enter numeric values only.") 
    
division = safe_divide(4,0)
print(division)

