student = []
 
while True:
    print("~~~~~ Student Attendance System ~~~~~")
    print("1. Add Student")
    print("2. View Students")
    print("3. Mark Attendance")
    print("4. View Attendance")
    print("5. Exit")

    Choice = int(input("Enter a Choice: "))

    if Choice>5 or Choice<1 :
        print("Error!! Choice a number between 1-5")
   
    if Choice == 1:
        print("~~~~~ Add Student ~~~~~")
        

        roll_no = int(input("Enter Roll Number: "))
        name = input("Enter Student Name: ")

        Students = {
            "roll_no" : roll_no,
            "name" : name,
            "attendance" : [],
        }

        student.append(Students)

        print("succesfully added!")
        print("------------------------")

    if Choice == 2:
        print("~~~~~ View Student ~~~~~")

        if len(student) == 0:
            print("No students added!")

        else:
            for Students in student:

                print("Roll Number:", Students["roll_no"])
                print("Name:", Students["name"])
                print("Attendance:", Students["attendance"])
                print("~~~~~~~~~~~~~~~~~~~~~~~~")

    if Choice == 3:
        print("~~~~~ Mark Attendance ~~~~~")

        Roll_no = int(input("Enter your roll number: "))

        if len(student) == 0:
            print("No students added!")

        else:
            for Students in student:
                if Students["roll_no"] == Roll_no:
                    print("------------------------")
                    print("1. present")
                    print("2. absent")

                    choice = int(input("Enter your choice: "))

                    if choice == 1:
                        Students["attendance"].append("present")
                        print("------------------------")
                        print("Attendance marked as present!")
                        print("------------------------")

                    elif choice == 2:
                        Students["attendance"].append("absent")
                        print("------------------------")
                        print("Attendance marked as absent!")
                        print("------------------------")

                    else:
                        print("Error! Choice a number between 1-2")

        if Roll_no != Students["roll_no"]:
            print("Roll number not found!")

    if Choice == 4:
        print("~~~~~ View Attendance ~~~~~")

        if len(student) == 0:
            print("No students added!")

        else:
            Roll_no = int(input("Enter your roll number: "))

            for Students in student:
                if Students["roll_no"] == Roll_no:

                    print("Attendance:", Students["attendance"])

                    present = Students["attendance"].count("present")

                    absent = Students["attendance"].count("absent")

                    Total = present + absent

                 else:
                     print("~~~~~~~~~~~~~~~~~~~~~~")
                     print("Days you were present:", present)
                      print("Days you were absent:", absent)
                    print("Total Days:", Total)
                    print("Attendance Percentage:", round(present/Total *100, 2), "%")
                    print("~~~~~~~~~~~~~~~~~~~~~~")

        if Roll_no != Students["roll_no"]:
                    print("Roll number not found!")

    if Choice == 5:
        print("Exiting the program...")
        break
