from django.urls import path
from api import views
from api.views import UploadFileView

urlpatterns = [

    
    path('invoices/',views.InvoiceView.as_view(),name='all_invoices'),
    path('invoices/upload/', UploadFileView.as_view(), name='upload-file'),
    path('invoices/add/',views.AddInvoice.as_view(),name='add_invoice'),
    path('invoices/<int:id>/',views.InvoiceDetailView.as_view(),name='single_invoice'),
    path('invoices/update/<int:pk>/',views.UpdateInvoice.as_view(),name='update_invoice'),
    path('invoices/delete/<int:pk>/',views.DeleteInvoice.as_view(),name='delete_invoice')
]

