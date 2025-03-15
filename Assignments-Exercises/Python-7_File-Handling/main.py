# Reading the sample text file
file_to_read = 'sample.txt'
try:
    with open(file_to_read, 'r') as file:
        content = file.read()
        print("Content of the file: ")
        print(content)
        file.close()

# Catch the error
except ValueError:
    print("File cannot be found.")


# Writing and creating a new file
new_file = 'newfile.txt'
with open(new_file, 'w') as file:
    file.write("Hello World, this is a test!")
    file.close()
    print(f"\n{new_file} is created")
    
# Reading the created file
file_to_read = new_file
try:
    with open(file_to_read, 'r') as file:
        content = file.read()
        print("\nContent of the file: ")
        print(content)
        file.close()

# Catch the error
except ValueError:
    print("File cannot be found.")

