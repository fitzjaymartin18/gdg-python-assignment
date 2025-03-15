# Function for greeting
def create_greeting(name):
    return f"Hello {name}"

try: 
    # Ask user name
    name = input("Name: ")

    # Store the resutl in a variable
    greeting =  create_greeting(name)
    
    # Print the result
    print(greeting)

# Catch error
except ValueError:
    print("Invalid input: Please enter a valid name.")