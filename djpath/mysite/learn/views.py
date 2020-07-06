from django.shortcuts import render
from django.http import HttpResponse

# homepage
def home(request):
	return render(request, 'home.html')

def index(request):
	return HttpResponse("Welcome to talkweb")
