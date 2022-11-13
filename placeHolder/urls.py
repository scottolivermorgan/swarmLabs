from django.conf.urls import url
from . import views
from django.urls import path




urlpatterns = [
	path('',views.landing, name='landing'),
	path('aboutUs/',views.aboutUs, name='aboutUs'),
	path('contact/',views.contact, name='contact'),
	path('register/',views.register, name='register'),
	path('comingSoon/',views.register, name='comingSoon'),
	path('shop/',views.shop, name='shop'),
	path('patents/',views.patents, name='patents'),

	
]







