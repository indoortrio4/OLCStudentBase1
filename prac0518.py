'''
### Task 1a : Square Integers

In wireless communication, the signal strength decreases as the distance 
from the transmitter increases. The decrease is proportional to the square 
of the distance, which is known as the inverse square law.

describing each step of signal loss, where *x* is the distance 
from the transmitter to receiver.

Write a user-defined function, `signal_loss(x)`, where *x* is an integer, 
that returns the number of square integers less than *x*. 
`signal_loss(x)` will return an integer.

E.g.  
*x* = 10 returns `3`.  
[4m]
'''
# def signal_loss(x):
#   number = 1
#   count = 0
#   while number**2 < x:
#     number += 1
#     count += 1
#   return count
# x = int(input("enter a number:"))
# y = signal_loss(x)
# print(y)




          

  
  
# def areacircle(x):
#   area = 3.14*x**2
#   return area
# circle1 = areacircle(14)
# circle2 = areacircle(89)
# circle3 = areacircle(55)
# print(circle1)
# print(circle2)
# print(circle3)
# circle 1 = 14, circle 2 = 89, circle 3 = 55

'''
### Task 1b : UI
Write a simple User Interface to do the following:
- Ask user to input a number, *x*.  
- Use `signal_loss()` and display the number of square integers in *dist* 
that are less than *x*.
- Repeatedly ask if the user wants to enter another number. 
- Quit the program when the user indicates that he or she does not want 
to enter another number.  

Appropriate input and output prompts must be included.  
[6m]
'''
# function calculate signal loss
# def signal_loss(x):
#   number = 1
#   count = 0
#   while number**2 < x:
#     number += 1
#     count += 1
#   return count

# # ui to ask again and again
# while True:
#   x = input("enter a number or type stop to end:")
#   if x == "stop":
#     break
#   else:
#     y = signal_loss(int(x))
#     print(y)
''' 
#### Task 2a : Repetitive Pattern
String Matching is the classical and existing problem. 
String matching strategies or algorithms provide a key role in 
various real world problems or applications. A few of its imperative applications 
are Spell Checkers, Spam Filters, Intrusion Detection System, Search Engines, 
Plagiarism Detection, Bioinformatics, Digital Forensics and 
Information Retrieval Systems etc.

A message, *s*, may contain corrupted characters during the transmission process 
(e.g. due to signal loss). Some clean-up processes may be employed to 
improve message integrity.

Write a user-defined function, `is_repetitive(s)`, where *s* is a string. 
The function will **only retain all characters that are letters and numbers**. 
All characters will be converted to lower case. 
The string *s* is said to have a 
repetitive pattern if both the halves of *s* are the same. 
If the length of *s* is odd, then the character in the middle of *s* is ignored. 
If *s* has a repetitive pattern, `is_repetitive(s)` will return the Boolean value `True`, 
and otherwise return `False`. Strings with 1 or less character will also return `False`.

E.g.   
"SGD$5S GD5" returns `True`.  # remove spaces sgd5sgd5
"abcdabc" returns `True`.  
"SST10SST" returns `False`.  
[6m]
'''

  

  # change to lower case
      

def is_repetitive(s):

  newstr = ''
  for char in s:
    if char.isdigit() or char.isalpha():
      newstr = newstr +char.lower()

  # part 2: start to check if first half == second half
  length = len(newstr) # find the length of the string
  midindex = length // 2 # find the middle index

  if length > 1:
    # check if length is even
    if length % 2 == 0:
      half1 = newstr[0:midindex] # first half of the string
      half2 = newstr[midindex:] # second half of the string
    else:
      # check if length is odd
      half1 = newstr[0:midindex] # first half of string
      half2 = newstr[midindex+1:] # second half of string

    # check if first half == second half
    if half1 == half2:
      return True
    else:
      return False
  else:
    print("Length of string is 1 or less, cannot check duplicate")
    return False

print(is_repetitive('SGD$5S GD5'))
print(is_repetitive('abcdabc'))
print(is_repetitive('SST10SST'))

  



'''
#### Task 2b : FileIO
In the file **Task2B_data.txt**, the first line contains a number, *n*.  
Subsequently, there are *n* number of lines, each contains a string.  

Write a program to read in **Task2B_data.txt**. For each string, display if the string 
has a repetitive pattern.  

Your program should use the `is_repetitive(s)` function.

Appropriate formatted output prompts must be included.  
[4m]
'''
