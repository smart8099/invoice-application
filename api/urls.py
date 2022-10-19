from django.urls import path
from . import views

urlpatterns =[
    path('',views.getInvoices),
    path('add/',views.addInvoice),
    path('invoice/<int:pk>/',views.get_invoice_detail)

]