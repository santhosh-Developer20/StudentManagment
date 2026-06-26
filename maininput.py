from studentinput import Addstudent
from courseinput import Addcourse
from tabulate import tabulate
from viewstudent import Viewstudent
from viewcourse import Viewcourse
from enrollmenrenview import Viewenroll
print("""=====================================
    STUDENT AND COURSE MANAGEMENT
=====================================""")
print("(ENTER OPTION '1' FOR STUDENTMANAGEMENT)")
print("(ENTER OPTION '2' FOR COURSEMANAGEMENT)")
print("(ENTER OPTION '3' FOR ENROLLMENTMANAGEMENT)")
while True:
    a=(input("Enter your Option : "))
    match a:
        case a if a=="1":
            print("""=================================
        STUDENTMANAGEMENT
=================================""")
            print("(ENTER OPTION '1' FOR ADD STUDENT)")
            print("(ENTER OPTION '2' FOR VIEW STUDENT)")
            b=input("Enter your Option : ")
            match b:
                case b if b=="1":
                    x=int(input("How many student to Add: "))
                    s=Addstudent(x)
                    
                    break
                case b if b=="2":
                    s=Viewstudent()
                    # s.viewingStudent()
                    # print(tabulate(data,headers="keys", tablefmt="fancy_grid"))

                    break

                case _:
                    print("invalid")
        case a if a=="2":
            print("""=================================
        COURSEMANAGEMENT
=================================""")
            print("(ENTER OPTION '1' FOR ADD COURSE)")
            print("(ENTER OPTION '2' FOR VIEW COURSE)")

            b=input("Enter your Option : ")
            match b:
                case b if b=="1":
                    y=int(input("HOW MANY COURSE WANT TO ADD: "))
                    c=Addcourse(y)
                    break

                case b if b=="2":
                     x=Viewcourse()
                     break
                case _:
                    print("invalid")
        case a if a=="3":
            print("""=================================
      ENROLLMENTMANAGEMENT
=================================""")     
            print("(ENTER OPTION '1' FOR VIEW ENROLLMENT)")
            print("(ENTER OPTION '2' EXIT)")

            c=input("Enter your Option : ")
            match c:          
                case c if c=="1":
                    y=Viewenroll()
                    break
                case c if c=="2":
                    break
                case _:
                    print("Invalid")
                    

        case _:
            print("invalid")