student = []
 
while True:
    print("~~~~~ Student Attendance System ~~~~~")
    print("1. Add Student")
    print("2. View Students")
    print("3. Mark Attendance")
    print("4. View Attendance")
    print("5. Exit")

    a = int(input("Enter a Choice: "))

    if a>5 or a<1 :
        print("Error!! Choice a number between 1-5")
   
    if a == 1:
        print("~~~~~ Add Student ~~~~~")
        

        roll_no = int(input("Enter Roll Number: "))
        name = input("Enter Student Name: ")

        abc = {
            "roll_no" : roll_no,
            "name" : name,
            "attendance" : [],
        }

        student.append(abc)

        print("succesfully added!")

    if a == 2:
        print("~~~~~ View Student ~~~~~")

        if len(student) == 0:
            print("No students added!")

        else:
            for abc in student:

                print("Roll Number:", abc["roll_no"])
                print("Name:", abc["name"])
                print("Attendance:", abc["attendance"])
                print("~~~~~~~~~~~~~~~~~~~~~~~~")

    if a == 3:
        print("~~~~~ Mark Attendance ~~~~~")

        c = int(input("Enter your roll number: "))

        if len(student) == 0:
            print("No students added!")

        else:
            for abc in student:
                if abc["roll_no"] == c:
                    print("------------------------")
                    print("1. present")
                    print("2. absent")

                    d = int(input("Enter your choice: "))

                    if d == 1:
                        abc["attendance"].append("present")
                        print("------------------------")
                        print("Attendance marked as present!")
                        print("------------------------")

                    elif d == 2:
                        abc["attendance"].append("absent")
                        print("------------------------")
                        print("Attendance marked as absent!")
                        print("------------------------")

        if c != abc["roll_no"]:
            print("Roll number not found!")

    if a == 4:
        print("~~~~~ View Attendance ~~~~~")

        if len(student) == 0:
            print("No students added!")

        else:
            f = int(input("Enter your roll number: "))

            for abc in student:
                if abc["roll_no"] == f:

                    print("Attendance:", abc["attendance"])

                    present = abc["attendance"].count("present")

                    absent = abc["attendance"].count("absent")

                    Total = present + absent

                    print("~~~~~~~~~~~~~~~~~~~~~~")
                    print("Days you were present:", present)
                    print("Days you were absent:", absent)
                    print("Total Days:", Total)
                    print("Attendance Percentage:", present//Total *100, "%")
                    print("~~~~~~~~~~~~~~~~~~~~~~")

    if a == 5:
        print("Exiting the program...")
        break