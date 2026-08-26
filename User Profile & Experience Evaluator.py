# 1. inputs
while True :
    name = input("Enter your name: ").strip()
    if name != "":
        break
    else :
        print("Please enter your name! ")
while True: 
    age_input = input("Enter your age: ")
    if age_input.isdigit() :
        age = int(age_input)
        break
    else :
        print("Please, enter a valid number for age!")

# Clean user name formatting
clean_name = name.title()

# 2. Age verification
if age < 18 :
    print("Sorry, registration is only available to people aged 18 and over.")
else :

    # 3. skill collection loop
    while True :
        count_input = input("How many skills do you have? (enter a number) ").strip()
        if count_input.isdigit() :
            skills_count = int(count_input)
            break
        else :
            print("Please enter a valid number! ")  
skills_list = []
for number in range(skills_count) :
    skill = input(f"Enter your skill number {number+1} (or 'stop' to finish): ").strip()

    # Skip empty inputs
    if skill == "" :
        continue

    # Exit loop if user types 'stop'
    if skill.lower() == "stop": 
        break
    skills_list.append(skill.title())

    # Update of the count of skills
    skills_count = len(skills_list)

# 4. Account  status & skill classification
status_of_account = input("Is your account active? ('yes' or 'no') ").strip().lower()
account_active = status_of_account == "yes"
account_inactive = status_of_account == "no"

# Check for Python skill in the list
if "python" in [s.lower() for s in skills_list] :
    classification = "Python developer"
else :
    classification = "General learner"

# Check experience conditions
if len(skills_list) > 2 and age > 20 and account_active :
    print(f"Congratulations {clean_name}, you have the required experience.")
elif not account_active :
    print(f"Sorry {clean_name}, your account is inactive. Please activate it first.")
else :
    print(f"Sorry {clean_name}, you don't have the required experience.")