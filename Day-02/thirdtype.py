##=> Without returntype and with arguments
##Reading => Main
##Printing => Function
##Logic => Functions
def noofdigits(v):
      print("Entered number is: {} and its"
      "digit count is: ".format(v),end=" ") 
      c = 0
      while v!=0:
            c+=1
            v//=10
      print("{}".format(c))
      return 

n = int(input("Enter a number: "))
noofdigits(n)
