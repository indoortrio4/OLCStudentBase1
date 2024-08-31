'''
Mock Question 1 (Task 2) 

The following program allows the entry of temperatures for a week. 
The program checks if the temperature is within a normal range (24°C to 28°C inclusive). 

days = 7 
normal_min = 24 
normal_max = 28 
for day in range(days): 
    temp = float(input("Enter the temperature for the day: ")) 
    if temp > normal_max: 
        print("The temperature is too high") 
    if temp < normal_min: 
        print("The temperature is too low") 

Open the file TEMPERATURE.py 
Save the file as MYTEMP_<your name><center number><index number>.py 

Qn1: Edit the program so that it: 

Accepts temperatures for only 5 days.  
[1 mark] 


Qn 2: Prints "The temperature is normal" when the temperature is between 24°C and 28°C inclusive.  
[2 marks] 


Qn 3: Counts and prints the number of days with temperatures too high and too low after all inputs.  
[4 marks] 

Save your program. 
Save your program as VARTEMP_<your name><center number><index number>.py 

Qn 4: Edit your program so that it works for any number of days. 

Save your program.  
[3 marks] 
'''
# while True:
#   days = input("enter the number of days: ")
#   if days.isdigit():
#     break
#   else:
#     print("enter numbers only")
#     continue

# normal_min = 24 
# normal_max = 28 
# counter1 = 0
# counter2 = 0
# for day in range(int(days)): 
#   temp = float(input("Enter the temperature for the day: ")) 
#   if temp > normal_max: 
#     print("The temperature is too high") 
#     counter1 = counter1 +1
#   elif temp < normal_min: 
#     print("The temperature is too low") 
#     counter2 = counter2 +1
#   else:
#     print("temperature is mornal")
# print("number of days with higher temperature: ",counter1)
# print("number of days with lower temperature: ",counter2)

#############################################################################
#############################################################################
#############################################################################
'''
Mock Question 2 (Task 2) 

The following program generates an email ID for a user. 
It creates the email ID by taking the first three letters of the user’s first name and appending 
it to the user's last name. It then verifies the user's email address. 

Program Code: 

firstname = input("Please enter your first name: ") 
lastname = input("Please enter your last name: ") 
email_id = firstname[:3] + lastname + "@example.com" 
print("Your email ID is " + email_id) 
email = input("Please enter your email address: ") 


Q1: Edit the program to ensure that the email ID is created using the first letter of the first name 
and the entire last name.  
[1 mark] 


Q2: The program needs to verify that the email address provided by the user is valid. 

Edit the program to: 
 Check if the email contains the '@' symbol. 
 Output a suitable error message if the email does not contain the '@' symbol, 
 and prompt the user to enter a valid email address repeatedly until the correct format is provided. 
[4 marks] 


Q3: Edit the program to: 
Ask the user to re-enter their email address. 
Check that the second entry of the email address matches the first entry. 
Output the message "Your email address has been confirmed." if the email entries match. 
Otherwise, output the message "Email addresses do not match. 
Please re-enter your email address: " and read the email address again, 
repeating this until the entries match. 
[5 marks] 

'''
# firstname = input("Please enter your first name: ") 
# lastname = input("Please enter your last name: ") 
# email_id = firstname[:1] + lastname + "@example.com" 
# # print("Your email ID is " + email_id) 

# entry of first email address to check
while True:
  email = input("Please enter your email address: ").lower()
  if '@' in email:
    print("email is correct")
    break
  else:
    print("email is incorrect. You must have an @ in the email")
    continue

# ask for email again, and check match the first email above
while True:
  email1= input("please re-enter yout email again: ")
  if email1 == email:
    print("email match")
    break
  else:
    print("email does not match")
    continue
    
  # x = input("please re-enter your email")
  #   if email in x:
  #     print("email is correct")
  #     break
  #   else:
  #     print("email does not match")
  #     continue
  