from operator import inv
from django.urls import is_valid_path
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from api.models import Invoice
from api.serializers import InvoiceSerializer
from api.pagination import CustomPagination




class InvoiceView(ListAPIView):
    queryset = Invoice.objects.all().order_by('id')
    serializer_class = InvoiceSerializer
    pagination_class = CustomPagination



@api_view(['POST'])
def addInvoice(request):
    serialized_invoice = InvoiceSerializer(data=request.data)

    if serialized_invoice.is_valid():
        serialized_invoice.save()

        return Response(serialized_invoice.data, status=status.HTTP_201_CREATED)
    return Response(serialized_invoice.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_invoice_detail(request, pk):
    try:
        invoice = Invoice.objects.get(pk=pk)
    except Invoice.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = InvoiceSerializer(invoice)
    return Response(serializer.data)


@api_view(['PUT'])
def update_invoice(request, pk):

    try:
        invoice = Invoice.objects.get(pk=pk)
    except Invoice.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serialized_invoice = InvoiceSerializer(invoice, data=request.data)

    if serialized_invoice.is_valid():
        serialized_invoice.save()
        return Response(serialized_invoice.data)
    return Response(serialized_invoice.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_invoice(request, pk):

    try:
        invoice = Invoice.objects.get(pk=pk)
    except Invoice.DoesNotExist:
        return Response(status=404)
    invoice.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)
 