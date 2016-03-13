from django.shortcuts import render

# Create your views here.

def index(request):
	
	return render(request,'index.html')

def lukyme(request):

	return render(request,'lukyme.html')

def lukynote(request):
	return render(request,'lukynote.html')
