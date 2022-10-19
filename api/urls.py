from django.urls import path
from api import views

urlpatterns = [

    
    path('invoices',views.InvoiceView.as_view()),
    path('invoices/add/',views.addInvoice),
    path('invoices/<int:pk>/',views.get_invoice_detail),
    path('invoices/update/<int:pk>',views.update_invoice),
    path('invoices/delete/<int:pk>',views.delete_invoice)
]

