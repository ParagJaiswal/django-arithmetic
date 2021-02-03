from django.urls import path
from . import views

urlpatterns = [
	path('',views.index,name='index'),
	path('option',views.maths,name='maths'),
	path('solution',views.logic,name='logic')
	
]