##=> With returntype and without arguments
##Reading => Function
##Printing => Main
##Logic => Functions
def noofdigits():
      v = int(input("Enter a number: "))
      print("Entered number is: {} and its"
      "digit count is: ".format(v),end=" ") 
      c = 0
      while v!=0:
            c+=1
            v//=10
      return c

print("{}".format(noofdigits()))
