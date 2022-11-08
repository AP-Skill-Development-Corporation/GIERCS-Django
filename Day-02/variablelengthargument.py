##Variable length argument

##def em(e,*y,**j):
##      print(e,type(e))
##      print(y,type(y))
##      print(j,type(j))
##      return
##
##em(lname='Tarun',12.45,3,45.0565,True,\
##   name='suresh',add='Rjy',sal=45000)


def em(**j):
      print(j,type(j))
      return

em(45,lname='Tarun',name='suresh',add='Rjy',sal=45000)
