from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def demo(g):
	return HttpResponse("Good Evening to All..")

def std(request,sname):
	return HttpResponse(f"Hello Student {sname}")

def emp(request,eage,ename):
	return HttpResponse(f"Hello Employee {ename} and your age is: {eage}")