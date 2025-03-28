while True:
    try:
        num1 = input("Enter a number (or type 'quit' to exit): ")
        if num1.lower() == 'quit':
            print("Goodbye!")
            break
        
        num2 = input("Enter another number: ")
        if num2.lower() == 'quit':
            print("Goodbye!")
            break
        
        result = int(num1) + int(num2)
        print(f"The total is: {result}")
    except ValueError:
        print("Invalid entry. Please enter a number with a numerical value.")
