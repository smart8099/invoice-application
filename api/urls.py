from django.urls import path
from api import views

urlpatterns = [

    
    path('invoices',views.InvoiceView.as_view(),name='all_invoices'),
    path('invoices/add/',views.addInvoice,name='add_invoice'),
    path('invoices/<int:pk>/',views.get_invoice_detail,name='single_invoice'),
    path('invoices/update/<int:pk>',views.update_invoice,name='update_invoice'),
    path('invoices/delete/<int:pk>',views.delete_invoice,name='delete_invoice')
]

