from django.shortcuts import render



def landing(request):
	return render(request, 'placeHolder/landing.html')
	
def aboutUs(request):
	return render(request, 'placeHolder/aboutUs.html')

def shop(request):
	return render(request, 'placeHolder/shop.html')
	
def patents(request):
	return render(request, 'placeHolder/patents.html')


def contact(request):
	return render(request, 'placeHolder/contact.html')
	
def register(request):
	return render(request, 'placeHolder/register.html')
	
def comingSoon(request):
	return render(request, 'placeHolder/comingSoon.html')