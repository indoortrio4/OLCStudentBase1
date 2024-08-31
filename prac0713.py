'''
The following program allows the weights of 15 bags of rice to be input. 
The correct weight for each bag of rice must be 
between 4.9 kg and 5.1 kg inclusive.
'''
# bags_rice = int(input("enter the amount of rice you are going to enter"))
# upper_bound = 5.1
# lower_bound = 4.9
# countunder = 0
# countover = 0
# for count in range(bags_rice):
#     bag_weight = float(input("Enter the weight of the bag of rice "))
#     if bag_weight <= upper_bound and bag_weight >= lower_bound:
#         print("the bag of rice is the correct weight")
#     if bag_weight > upper_bound:
#         print("The bag of rice is overweight")
#         countover = countover+1
#     if bag_weight < lower_bound:
#         print("The bag of rice is underweight")
#         countunder = countunder + 1      
# print("the number of bags that are underweight is", countunder)
# print("the number of bags that are overweight is", countover)
'''
Open the file RICEBAGS.py
Save the file as MYBAGS_<your name>_<center number>_<index number>.py

1.	Edit the program so that it:
a.	Accepts the weights for only 10 bags of rice.
[1]
'''

'''
b.	Prints out the message “The bag of rice is the correct weight” 
when a weight entered is between 4.9kg and 5.1 kg inclusive.
[2] 
'''

'''
c.	Prints out the number of bags of rice that were underweight, 
as well as the number that were overweight, after the weights of 
all the bags have been entered.
[5]
'''

'''
Save your program.
2.	Save your program as VARBAGS_<your name>_<center number>_<index number>.py
Edit your program so that it works for any number of bags of rice.
Save your program.
[2]
'''
## TO READ TO A FILE
# fobj = open("cyberattacks.txt",r")
# contents = fobj.read()
# print(contents)

## WRITE TO A FILE
fobj = open("cyberattacks2.txt","w")
fobj.write("rlkfsjdlkfjsdlkfjlkdj")
fobj.close()



## open the file cyberattacks.txt
# count the number of vowels in the file
# how any a, e , i o, u
# output the answer to a file called vowelcount.txt
a = 0
e=0
i = 0
o = 0
u = 0
fobj = open ("cyberattacks.txt")
contents = fobj.read()
for p in contents:
    if p == "a" or p == "A":
        a = a +1
    elif p == "e" or p == "E":
        e = e + 1
    elif p == "i" or p == "I":
        i = i +1
    elif p == "o" or p == "O":
        o = o + 1
    elif  p == "u" or p =="U":
        u = u+1
print (a)    
print(e)   
print(i) 
print(o) 
print(u) 
fobj = open("vowelcount.txt","w")
strcount = "A:{}, E:{}, I: {}, O:{},U:{}".format(a, e, i, o, u)

fobj.write(strcount )
fobj.close()