##Argument types
##      - Default
##      - Required or Positional
##      - Keyword
##      - variable Length

def studentdetails(r,n,b="CS",y=3):
      print("Student Details:" )
      print(f"Roll Number is: {r}")
      print(f"Name is: {n}")
      print(f"Branch is: {b}")
      print(f"Year is: {y}")
      return

roll = input("Enter Roll Number: ")
name = input("Enter Name: ")
branch = input("Enter branch: ")
year = input("Enter Year: ")
studentdetails(roll,name,branch,year)
