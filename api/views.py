from encodings import search_function
from operator import inv
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,CreateAPIView,ListCreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from api.models import Invoice
from api.serializers import InvoiceSerializer, InvoiceFileUploadSerializer
from api.pagination import CustomPagination
import io,csv
import pandas as pd
from rest_framework.filters import SearchFilter


class UploadFileView(CreateAPIView):
    serializer_class = InvoiceFileUploadSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file)
        for _, row in reader.iterrows():
            new_invoice = Invoice(
                       expiration_date = row['Expiration Date'],
                       invoice_items_count = row["Number of Invoices"],
                       recipient_name = row["Recipient Name"],
                       description = row["Description"]
                       )
            new_invoice.save()
        return Response({"status": "success"},
                        status.HTTP_201_CREATED)

class InvoiceView(ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    pagination_class = CustomPagination
    filter_backends = [SearchFilter]
    search_fields = ('recipient_name','description')


class AddInvoice(CreateAPIView):
    serializer_class = InvoiceSerializer
    



class InvoiceDetailView(RetrieveAPIView):
    lookup_field = "id"
    serializer_class = InvoiceSerializer
    queryset =  Invoice.objects.all()

class UpdateInvoice(UpdateAPIView):
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()


class DeleteInvoice(DestroyAPIView):
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()


