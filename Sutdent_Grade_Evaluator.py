while True:
    try:
        grade = float(input("Score: "))
        
        if grade > 100 or grade < 0:
            print("Error: Grade out of range")
            continue
            
        if grade >= 90:
            print("Grade: A")
            
        elif grade >= 80:
            print("Grade: B")
            
        elif grade >= 70:
            print("Grade: C")
            
        elif grade >= 60:
            print("Grade: D")
            
        elif grade < 60:
            print("Grade: F")
            
        else:
            raise ValueError("Invalid Input")
            continue
        
    except ValueError as ve:
        print("Error:", ve)
        continue
    
    again = input("Enter another score (yes/no)? ").lower()
    if again != "yes":
        print("Goodbye...")
        break