# For Loop section
favorite_books = ["The Great Gatsby", "Atomic Habits", "Rich Dad Poor Dad", "12 Rules of Life", "Make it stick", "Deep Work", "What it is all about?"]

for book in favorite_books:
    print(book)

# While Loop section
try:
    number = int(input("Number: "))
    
    if 0 < number:
        while 1 <= number:
            if number == 1:
                print("Countdown complete!")
                break
            
            print(number)
            number -= 1
            
    else:
        print("Invalid input: Please enter a number greater than zero.")
except ValueError:
    print("Invalid input: Please enter a positive integer.")



