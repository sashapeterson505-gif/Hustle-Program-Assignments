# Sasha Peterson | Lab 4 | Intro to Python

# Ticket 1

# PREDICT: 17, 25, and maybe 13 will get accepted 

from operator import index


ages = [17, 11, 25, 13, 9]
for age in ages:
    if age >= 13:
        print(f"[ACCEPTED] Age: {age}")
    else:
        print(f"[REJECTED] Age: {age}")

# EXPLAIN: i dont rlly understand the question but i think each number from the age list is being compared to 13 and if its greater then or equal, it gets accepted

# Ticket 2

# PREDICT: no i dont think the loop will run at all. 

keep_checking = "yes"
while keep_checking == "yes":
   age = int(input("Enter age: ")) 
   if age >+ 13:
       print("ACCEPTED")
   else:
       print("REJECTED")
       keep_checking = input("Check another age? (yes/no): ")

# EXPLAIN: because u use a while loop when u wnat to keep doing something until something specific happens. 

# Ticket 3

# PREDICT: yes the loop would run forever bc it would keep asking for a age. 

while True:
    user_input = input('Enter age or type "stop" to exit: ')
    if user_input == "stop":
        break
    age = (user_input)
    if age < 0:
        print("age can't be too low.")
    if age < 18:
        print("Your a minor")
    if age < 65:
        print("Your an adult.")
    else:
        print("Your a senior citizen.") # when i fixxed my code using the problems at the bottom, it changed some of my code and whenever i changed it back my code wouldnt run so i left it alone.

# EXPLAIN: one loops stopped based on the while statment and the other uses while true and needs break to stop or it will keep going. 

 # Ticket 4

# PREDICT: the output looks the same because ur age determines if u get access or not. but im pretty sure both code structures are different but similar.

def can_access(age):         # defining the function
    if age >= 13:
        return True
    else:
        return False 
    
ages = [17,11,25,13,9] #same list as before 
for age in ages: 
    if can_access(age): 
        print(f"{age} is ACCEPTED")
    else: 
        print(f"{age} is REJECTED")

# EXPLAIN: when u write the function once, then u can use it whenever u need it so u dont have to keep rewriting it. 

# Ticket 5 

# PREDICT: signup #1| age 22 - accepted, signup #2| age 10 - rejected, signup #3| age 15 - rejected, signup #4| age 8 - rejected, signup #5| age 19 - accepted, signup #6 age 13 - rejected 
# approved: 2 out of 6 

def signup_report(ages_list): # keep track of how many people signed up and how many were approved
    approved_count = 0
    for index, age in enumerate(ages_list): #i cant run my code without this but its auto putting this even when i do esc, this keeps happening im not sure why 
        signup_number = index + 1 # starting at 1
        if can_access(age):
            print(f"Signup #{signup_number} | age {age} - ACCEPTED")
            approved_count += 1
        else:
            print(f"Signup #{signup_number} | age {age} - REJECTED")
    print(f"approved: {approved_count} out of {len(ages_list)}")

signups = [22, 10, 15, 8, 19, 13]
signup_report(signups)

# EXPLAIN: functions, loops, variables, enumerate?, f-strings, lists, if, return, print
