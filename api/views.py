from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from rest_framework.decorators import api_view
from .models import Invoice
from.serializers import InvoiceSerializer


@api_view(['GET'])
def getInvoices(request):
    paginator = PageNumberPagination()
    #paginator.page_size = 10
    invoice = Invoice.objects.all()
    result_page = paginator.paginate_queryset(invoice,request)
    
    serialized_invoice = InvoiceSerializer(result_page, many=True)
    return Response(serialized_invoice.data,status=status.HTTP_200_OK)
   

    