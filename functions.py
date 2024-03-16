#python functions
##Python function is a modular piece of code that can be used repeatedly.
# Generally a function is a block of code which is executed when it is called from somewhere in the program.
# A function has a return value.
#Functions are perfect for abstraction. They allow us to write blocks of code which can be reused in different ways and in different programs.

#function that adds two numbers
def add_nums(a,b):
    result=a+b
    return result
print(f'The sum is {add_nums(60,66)}')


#Arbitrary Arguments, *args If you do not know how many arguments that will be passed into your function, 
#add a * before the parameter name in the function definition.
def addition(*numbers):
    sum=0
    for i in numbers:
        sum+=i
        return sum
print(f'total is {addition(23,44,-90,0,76,87,98)}')

#Arbitrary Keyword Arguments, **kwargs
#If the keyword arguments to be passed in a function are not known,
#you should add ** before the parameter name in the function definition. Example: **age

def add_ages(**ages):
    ax=0
    for _,l in ages.items():
        ax+=l
    return ax
print(f'Total is: {add_ages(Beno=18, Myra=19, Ezra=19, Abdul=20, Wahu=19)}')

#scopes#nested functions
def add_nums(x, y):  # Function to add two numbers
    answer = x + y  # Calculate the sum of x and y
    def double_it():  # Inner function to double the result
        double = answer * 2  # Double the result
        print(double)  # Print the doubled result
    double_it()  # Call the inner function to double the result
    return answer  # Return the original sum

# Call the add_nums function with arguments 2 and 13
print(add_nums(2, 13))

