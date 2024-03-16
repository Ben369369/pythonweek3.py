#A lambda function is a special type of function without a name
#Lambda functions are efficient whenever you want to create a function that will only contain simple expressions – that is, expressions that are usually a single line of a statement.
#They're also useful when you want to use the function once.

#no parameters
peanuts=lambda:print('njugu')
print(peanuts())

#with parameters
square_root=lambda numero:numero**2
print(square_root(60))

#lamda function with parameter to determine whether a word is a palindrome
ispalindrome=lambda word:"The word is a palindrome" if word==word[::-1] else "not a pallindrome"
word=input(" enter word to determine whether it is a pallindrome: ")
print(ispalindrome(word))
