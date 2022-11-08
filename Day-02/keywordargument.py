##Keyword argument

def studentdetails(n,r):
      print("Student Details are: ")
      print(f"Student Roll Number : {r}")
      print(f"Student Name: {n}")
      return

roll = input("Enter Roll Number: ")
name = input("Enter Name: ")
studentdetails(r=roll,n=name)
