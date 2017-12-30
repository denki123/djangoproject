from django.shortcuts import render

def index(request):
	return render(request, 'personal/home.html')
	
def asus(request):
	return render(request, 'personal/ASUS.html')

def acer(request):
	return render(request, 'personal/ACER.html')

def lenovo(request):
	return render(request, 'personal/LENOVO.html')
