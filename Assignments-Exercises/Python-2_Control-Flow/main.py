
try: 
    # Ask the user age
    age = int(input("Age: "))

    # Check age category
    if 0 < age < 13:
        print("You are categorized as: Child")
    elif 13 <= age <= 19:
        print("You are categorized as: Teenager")
    elif 20 <= age <= 59:
        print("You are categorized as: Adult")
    elif 60 <= age:
        print("You are categorized as: Senior")
    
    # Check age if negative
    else:
        print("Invalid input: Age cannot be negative") 

# Check if input is non-number
except ValueError:
    print("Invalid input: Age cannot be a non-number")