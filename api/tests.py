from cgi import test
import json

from django.urls import reverse
from rest_framework import status
from api.views import Invoice



class ListAllInvoicesTestCase(APITestCase):

    def test_invoice_view(self):
        response = self.client.get(reverse('all_invoices'))

        self.assertEqual(response.status_code,status.HTTP_200_OK)


class CreatePostInvoiceTestCase(APITestCase):

    def test_create_invoice(self):
        test_data ={
                    "expiration_date": "2022-10-22",
            "invoice_items_count": 163,
            "recipient_name": "Amanda Hodges",
            "description": "Question situation leg feel drop early want whether.\n"
             "Result close project think. Group mind she culture computer remain."}
        
        url = reverse('add_invoice')
        response = self.client.post(url,test_data,fomat=json)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Invoice.objects.count(), 1)
        self.assertEqual(Invoice.objects.get().recipient_name, 'Amanda Hodges')
        print(response.data)
       

     