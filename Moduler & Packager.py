from datetime import datetime
import time
import math
import random
import string
import uuid

def datetime_menu():
    while True:
        print("... Datetime and Time Operations...")
        print("1. Show Current Date and Time")
        print("2. Calculate Difference Between Two Dates/Times")
        print("3. Format Date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Exit")

        ch = int(input("Enter your choice: "))

        if ch == 1:
            print("Current Date and Time:", datetime.now())
        elif ch == 2:
            d1 = input("Enter first date (YYYY-MM-DD): ")
            d2 = input("Enter second date (YYYY-MM-DD): ")
            date1 = datetime.strptime(d1, '%Y-%m-%d')
            date2 = datetime.strptime(d2, '%Y-%m-%d')
            d = abs(date2 - date1)
            print("Difference:", d)
        elif ch == 3:
            print("Formatted Date:", time.ctime())
        
        elif ch == 4:
            input("start...")
            start = time.time()

            input("stop...")
            end = time.time()
            
            elapsed = end - start 
            
            min = int(elapsed // 60)
            sec = int(elapsed % 60)

            print(f"Elapsed time: {min} minutes {sec} seconds")
        
        elif ch == 5:
            sec = int(input("Enter countdown time in seconds: "))

            for i in range(sec, 0, -1):
                print("Time left:", i, "seconds", end="\r")
                time.sleep(1)

            print("\nTime's up!")
        
        elif ch == 6:
            break
    
def math_menu():
    while True:
        print("\n ..Mathematical Operations..")
        print("1. Basic Arithmetic")
        print("2. Trigonometry (sin, cos, tan)")
        print("3. Factorial")
        print("4. Logarithm")
        print("5. Interest Calculator")
        print("6. Geometric Shapes (Area & Perimeter)")
        print("7.Exit")
            
        ch = int(input("Enter your choice: "))

        if ch == 1:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print(f"Add: {a + b}, Sub: {a - b}, Mul: {a * b}, Div: {a / b}")
        
        elif ch == 2:
            a = float(input("Enter angle in degrees: "))
            rad = math.radians(a)
            print(f"sin: {math.sin(rad)}, cos: {math.cos(rad)}, tan: {math.tan(rad)}")
        
        elif ch == 3:
            n = int(input("Enter a number: "))
            print(f"Factorial: {math.factorial(n)}")
        
        elif ch == 4:
            n = float(input("Enter a number: "))
            base = float(input("Enter base (default is e): ") or math.e)
            l = math.log(n, base)
            print("Log:" ,l)
        
        elif ch == 5:
            p = float(input("Principal: "))
            r = float(input("Rate (%): "))
            t = float(input("Time (years): "))
            n = float(input("Compounded per year: "))
            amount = p * (1 + r / (100 * n))**(n * t)
            print(f"Compound Interest Amount: {amount:.2f}")

        elif ch == 6:
            while True:
                print("\n...Geometric Shapes...")
                print("1. Square")
                print("2. Rectangle")
                print("3. Circle")
                print("4. Triangle")
                print("5. Exit")
                shape = int(input("Choose shape: "))

                if shape == 1:
                    side = float(input("Enter side length: "))
                    print(f"Area: {side**2}, Perimeter: {4*side}")
                
                elif shape == 2:
                    l = float(input("Enter length: "))
                    w = float(input("Enter width: "))
                    print(f"Area: {l*w}, Perimeter: {2*(l+w)}")
                
                elif shape == 3:
                    radius = float(input("Enter radius: "))
                    print(f"Area: {math.pi*radius**2:.2f}, Circumference: {2*math.pi*radius:.2f}")
                
                elif shape == 4: 
                    a = float(input("Enter side a: "))
                    b = float(input("Enter side b: "))
                    c = float(input("Enter side c: "))
                    s = (a + b + c)/2
                    area = math.sqrt(s*(s-a)*(s-b)*(s-c)) 
                    print(f"Area: {area:.2f}, Perimeter: {a+b+c}")
                
                elif shape == 5:
                    break
                else:
                    print("Invalid shape choice.")
                
        
        elif ch == 7:
            break
        else:
            print("Invalid option.")


def random_menu():
    while True:
        print("\n..Random Data Generation..")
        print("1. Generate Random Number")
        print("2. Random Password")
        print("3. Random Sample from List")
        print("4. Generate OTP")
        print("5.Exit")
        
        ch = int(input("Enter your choice: "))

        
        if ch == 1:
            print("Random number (1-100):", random.randint(1, 100))
        
        elif ch == 2:
            length = int(input("Enter password length: "))
            chars = string.ascii_letters + string.digits + string.punctuation

            password = ""
            for _ in range(length):
                password = password + random.choice(chars)

            print("Password:", password)
        
        elif ch == 3:
            data = input("Enter comma-separated values: ").split(',')
            sample = random.sample(data, k=min(3, len(data)))
            print("Sample:", sample)

        elif ch == 4:
            otp = ""
            for _ in range(6):
                otp = otp + random.choice(string.digits)

            print("OTP:", otp)
        elif  ch == 5:
            break
        else:
            print("Invalid option.")

def uuid_menu():
    while True:
        print("\n...UUID Generation...")
        print("1. Generate UUID4")
        print("2. Generate Multiple UUIDs")
        print("3.Exit")
        
        ch = int(input("Enter your choice: "))
        
        if ch == 1:
            print("UUID4:", uuid.uuid4())
        elif ch == 2:
            count = int(input("How many UUIDs? "))
            for _ in range(count):
                print(uuid.uuid4())
        elif  ch ==3:
            break
        else:
            print("Invalid option.")

def file_menu():
    while True:
        print("\n...File Operations...")
        print("1. Write to File")
        print("2. Read from File")
        print("3. Append to File")
        print("4.Exit")

        ch = int(input("Enter your choice: "))
        filename = input("Enter filename (with extension): ")

        if ch  == 1:
            content = input("Enter content to write: ")
            with open(filename, 'w') as f:
                f.write(content)
            print("Written successfully.")
        elif ch == 2:
            with open(filename, 'r') as f:
                print("File Content:\n", f.read())
        elif ch == 3:
            content = input("Enter content to append: ")
            with open(filename, 'a') as f:
                f.write(content + "\n")
            print("Appended successfully.")
        elif  ch ==4:
            break
        else:
            print("Invalid option.")

def explore_modules():
    mod_name = input("Enter module name(like math,datetime):")
    try:
        print(dir(__import__(mod_name)))
    except ModuleNotFoundError:
        print("Module not found.")


def main():
    while True:
        print("\n... Multi-Utility Toolkit ...")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")

        ch = int(input("Enter your choice: "))

        if ch == 1:
            datetime_menu()
        elif ch == 2:
            math_menu()
        elif ch == 3:
            random_menu()
        elif ch == 4:
            uuid_menu()
        elif ch == 5:
            file_menu()
        elif ch == 6:
            explore_modules()
        elif ch == 7:
            print("Exit..Thank you")
            break
        else:
            print("Invalid choice..")

if __name__ == '__main__':
    main()