num=int(input("enter a number:"))
rev=0
while num!=0:
      if  (num%10)%2==0:
            rev=rev*10+num%10
      num//=10
##print("reverese number:",rev)
print("even numbers are:::",end=" ")
while rev!=0:
      print(rev%10,end=" ")
      rev//=10
