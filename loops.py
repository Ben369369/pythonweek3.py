no= [1,21,2,6,5,8]
for x in no:
    print (x)

#A range is a series of values between two numeric intervals.
#We use Python's built-in function range() to define a range of values.
#For example,
#five_steps = range(5)
# five_steps is now a collection with 5 elements:
# 0, 1, 2, 3, 4
welcome_message='Welcome to Nairobi'
for i in range(10):
    print(welcome_message)

#While Loops
#A while loop performs a set of instructions as long as a given condition is true.
    
x=0
while x <= 2:
    print(x)
    x += 1
else:
    print('yep you have reached 3 now')

# pick something from a list
clothes_colors=['blue','red','pink','purple','black']
desired_color='pink'
for colors in clothes_colors:
    if colors == desired_color:
        print('yeah that is the color ')
        break
    print(colors)

#using while loop
length=len(clothes_colors)
print(length)
count=0

while count<length:
    print(clothes_colors[count])
    if clothes_colors[count]==desired_color:
        print('oh! yeah!')
        break
    count +=1

#continue
# code to admit people above 21 0nly into the club

ages=[21,32,45,67,18,14,23,14,66,20,20.5,21.01]
for d in ages:
    if d<=21:
        continue# continue will skip ages below 21 and continue scanning the whole list and brings out only those over 21
    print(d)

# using break instead of continue
ages=[32,45,21,67,18,14,23,14,66,20,20.5,21.01]
for e in ages:
    if e<=21:
        break# the code will not continue scanning after finding the first age below 21
    print(e)

#nested loops
birds=[['pigeon','hawk'],['dove','sagehen']]
for f in birds:
    for g in f:
        print(g)

#list comprehensions
#code that iterates and doubles a list of numbers
nos = [2,4,-56,77,24,14,-66,67]
doubled_nos=[]

for numbers in nos:
    doubled_nos.append(numbers*2)

print(doubled_nos)

#OR Better
doubled=[nums*2 for nums in nos]
print(doubled)# shorter and less time consuming