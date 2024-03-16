base = float(input('Enter base: '))  # Convert input to float
exponent = float(input('Enter exponent: '))  # Convert input to float

def exponential(base, exponent):
    result = base ** exponent  # Use ** for exponentiation
    return result

x= exponential(base, exponent)  # Call the function to get the result

if x > 5000:
    print(True)  # Print True if the result is greater than 5000
else:
    print(False)  # Print False otherwise