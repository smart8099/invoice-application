from typing import ItemsView
from unittest.mock import seal
from rest_framework import serializers
from api.models import Invoice


class InvoiceFileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields  = ['expiration_date','invoice_items_count','recipient_name','description']
