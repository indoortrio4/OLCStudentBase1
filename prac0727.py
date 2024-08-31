'''
for loop recap practice

Using for loop print the pattern
do 
re 
mi 

do 
re 
mi

do 
re 
mi
---------------------------------------
do 
mi 
mi 
mi 

do 
mi 
mi 
mi 

do 
mi 
mi 
mi
'''

for i in range(3):
    print("do")
    for x in range(3):
        print("mi")
    


'''
Question 20: Print the following using a for loop.
example input:
APPLE
expected output:
A
AP
APP
APPL
APPLE
'''
## Write and test your code here
### for every variable i in the range of 10
# for i in range(10): #0,1,2,3,4,5,6,7,8,9
#     print(i)

# range(stop) 
word = ("apple")
for i in range(6):
    print(word[0:i])
# range(start, stop)
# word = "apple"
# for word in range(1,7):
#     print(word[:0])

##################### STRING SLICING ##################
### is slicing part of a word into sub parts



# word = "APPLE"
# print(word[:1])
# print(word[:2])
# print(word[:3])

# for i in 

# range(start, stop, step)
for i in range(3, 37, 3):
    print(i)

# print multiples of 5 from 5 to 60
for i in range(5, 60, 5):
    print(i)

'''
Question 21: Print the following pattern using nested for loops.
example input:
None
expected output:
* * * * *
* * * *
* * *
* *
*
'''
## Write and test your code here
x = "*"
for i in range(6,0,-1):
    print(x * i)
'''
Q2
You are given a list of computing paper 1 marks and paper 2 marks

paper1 = {"Ken": 80, "Mike": 84, "Ash": 55, "Zee": 65}
paper2 = {"Ken": 88, "Mike": 64, "Ash": 65, "Zee": 85}

Design a program to

1a.  update Ken's computing mark to 83 for paper 1 
1b.  update Mike's computing mark to 58 for paper 2 

2.  show the average of paper 1 marks and average of paper 2 marks

3.  ask user to enter a person and the paper he wants to search. 
If the person is in the list, show the respective mark.
Otherwise shows that the person cannot be found
'''

paper1 = {"Ken": 80, 
          "Mike": 84, 
          "Ash": 55, 
          "Zee": 65} # dictionary

paper2 = {"Ken": 88, "Mike": 64, "Ash": 65, "Zee": 85}

# retrieve the score for Ken
print(paper1["Ash"])

# change the value of Ken
paper1["Ken"] = 83
print(paper1)
paper1["Mike"] = 58

# loop through the key values using for loop
sum = 0
count = len(paper1)
for student in paper1:
    print(student) # prints the key
    print(paper1[student]) # retrieve the value for each student
    sum = sum +paper1[student]
print(sum)/len(paper1)
# TYPES OF VARIABLE
# var1 = "dog" # string variable
# var2 = "cat"
# var3 = var1 + var2
# print(var3)

# var4 = "10"
# var5 = 20
# var6 = var4 + var5
# print(var6)
