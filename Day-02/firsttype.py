##=> With returntype and with arguments
##Reading => Main
##Printing => Main
##Logic => Functions
def noofdigits(v):
      c = 0
      while v!=0:
            c+=1
            v//=10
      return c

n = int(input("Enter a number: "))
print("Entered number is: {} and its"
      "digit count is: {}".format(n,noofdigits(n)))
