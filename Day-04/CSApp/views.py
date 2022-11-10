from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def demo(g):
	return HttpResponse("Good Evening to All..")

def std(request,sname):
	return HttpResponse(f"Hello Student {sname}")

def emp(request,eage,ename):
	return HttpResponse(f"Hello Employee {ename} and your age is: {eage}")

def edy(e,empid,esal,ename):
	return HttpResponse(f"<h3>Employee Name: <span style='color:red'>{ename}</span><br/> Employee Id: <span style='color:green'>{empid}</span> <br/>Employee Salary: <span style='color:blue'>{esal}</span></h3>")

def dy(rq):
	return HttpResponse("<html><head><title>Demo Page</title></head><body><h3>Example for Html Structure</h3></body></html>")

def hy(rq,bm):
	return HttpResponse(f"<html><head><title>Sample Page</title></head><body><h3>Example for Html Structure</h3><h4>{bm}</h4></body></html>")

def stu(k,sid):
	return HttpResponse("<html><head><title>Demo page</title><style>h4{color:green}</style></head><body><h3>Example for Html Structure</h3><h4>"+str(sid)+"</h4></body></html>")

def gp(request,j):
	return HttpResponse(f"<html><head><script>alert('Hi Welcome {j}')</script></head><body><h4> Welcome {j}</h4></body></html>")

def sh(request,j,age):
	return HttpResponse(f"<html><head><script>alert('Hi welcome {j} \\nYour age is: {age}')</script></head></html>")

def sai(request):
	return render(request,'demo.html')

def empdetails(request,ename,empid,eage):
	return render(request,'emp.html',{'en':ename,'eid':empid,'ea':eage})

def streg(request):
	return render(request,'stregistration.html')