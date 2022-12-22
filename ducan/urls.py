from django.urls import path
from ducan.views import *

from . import views

app_name = 'ducan'

urlpatterns = [
        #Leave as empty string for base url
	path('', views.store, name="ducan"),
	path('kosarica/', views.cart, name="kosarica"),
	path('blagajna/', views.checkout, name="blagajna"),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
	path('Customers/', Customer),

]

