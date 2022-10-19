from typing import ItemsView
from unittest.mock import seal
from rest_framework import serializers
from api.models import Invoice

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields  = '__all__'
