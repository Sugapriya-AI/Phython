class multiple_functions():
    def subfields():
        print("Sub-fields in AI are: ")
        lists = ["Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language processing"]
        for x in lists:
            print(x)
            
    def OddEven():
        num=int(input("Enter the number: "))
        if num%2==0:
            print(num, "is Even number")
            message="Even number"
        else:
            print(num, "is Odd number")
            message="Odd number"
        return message 

    def marriage_eligibility():
        print("Welcome to the Marriage Eligibility Checker!")
        name = input("Enter your name: ")
        gender = str(input("Enter your gender (M/F): ")).upper()
        age = int(input("Enter your age: "))
        if (gender == "M") and (age >= 21):
            print(f"Congratulations {name}! You are eligible for marriage.")
        elif (gender == "F") and (age >= 18):
             print(f"Congratulations {name}! You are eligible for marriage.")
        else:
            print(f"Sorry {name}, you are not eligible yet.")

    def calculate_percentage():
        subject1=int(input("Subject1= "))
        subject2=int(input("Subject2= "))
        subject3=int(input("Subject3= "))
        subject4=int(input("Subject4= "))
        subject5=int(input("Subject5= "))
        total=subject1+subject2+subject3+subject4+subject5
        print("Total : ", total)
        percentage=total/5
        print("percentage : ",percentage) 

    def triangle():
        print("Area of the triangle")
        height=int(input("Height:"))
        breadth=int(input("Breadth:"))
        area=(height*breadth)/2
        print("Area of Triangle: ",area)
        print("Perimeter of the triangle")
        height1=int(input("Height1:"))
        height2=int(input("Height2:"))
        breadth=int(input("Breadth:"))
        perimeter=height1+height2+breadth
        print("Perimeter of Triangle:",perimeter)
