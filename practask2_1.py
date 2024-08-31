'''
A class has 10 students. The following program allows a teacher to input the favourite color 
of each students in the class.

num_students = 10
for x in range(num_students):
  colour = input(“What is the student’s favourite colour?”)

Qn 1. Edit the program to use a conditional loop that repeats until the teacher does not want to 
enter any more colours. Suitable input messages must be used.
Save your program [3 marks]


Qn 2. Edit your program to convert each colour to lower case and then store it into a list.
Save your program [2 marks]


Qn 3. Edit your program to display the number of students that have a specific favourite colour.
The program must:
Ask the teacher to input a colour to search for in the list.
Output the colour and the number of students who have that specific colour as their favourite colour.
Suitable input and output messages must be used.
Save your program. [5 marks]
'''
student = []
while True:
  colour = input('What is the student’s favourite colour? or type stop to break: ').lower()
  if colour == "stop":
    break
  else:
    student.append(colour)
# print(student)

# ask teacher to input a color
select = input(" what colour are you searching for").lower()

# is the color that teacher input in the list
if select in student:
  print("colour is in the list")

  # count the number of times that the color appear in the list
  # output this number of times for the color
  # temp variable to count
  count = 0
  for color in student:
    if color == select:
      count = count+1
     
  print(count, "students like this colour",select)   
else:
  print(select,"is not in the list")
      
      #print(selectedcolor, ':', colorcount)
 



