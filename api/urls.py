from django.urls import path
from . import views

urlpatterns =[
    path('',views.getInvoices),
    path('add/',views.addInvoice)

]