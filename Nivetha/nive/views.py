from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Person


def form(request):
	return HttpResponse('<h1><HII I"M NIVE/h1>')
# Create your views here.
def index(request):
	print(request.POST)
	return render(request, "ho.html")

from .forms import MemberForm
def create_data(request):
	if request.method == 'POST':
		form = MemberForm(request.POST)
		if form.is_valid():
			print("HI")
			form.save()
			return redirect("/create")
		else:
			print("error")	
	else:
		form = MemberForm()
		return render(request,"create.html",{'form':form})

 
def sample(request):
	if request.method == 'POST':
		data = request.POST
		print(data['firstname'])
		print(data['lastname'])
		print(data['phone'])
		print(data['email'])
		print(data['date'])
		print(data['password'])
		fname=data['firstname']<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
		print("fiiiiiii")
		Person.objects.create(firstname=fname,lastname=lname,phone=phno,email=email,date=date,password=password)
		# table=Member(username=name,password=password)
		# table.save()

	return render(request,"sample.html")

def login(request):
	if request.method == 'POST':
		login = request.POST
		print(login['email'])
		print(login['password'])
		
		email=login['email']
		password=login['password']
		
		Person.objects.create(email=email,password=password)
	return render(request,"ho.html")

