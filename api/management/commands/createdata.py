
from django.core.management.base import BaseCommand
from faker import Faker
import faker.providers
import faker.providers
from api.models import Invoice

class Command(BaseCommand):
    help = "Command information"

    def handle(self, *args, **options):

        fake = Faker()
        for _ in range(200):
            expiration_date = fake.future_date()
            invoice_items_count = fake.random_int(0,500)
            recipient_name = fake.name()
            description = fake.text()

            Invoice.objects.create(expiration_date=expiration_date,invoice_items_count=invoice_items_count,recipient_name=recipient_name,description=description)
        
        count_of_added_invoices = Invoice.objects.all().count()

        print(f'{count_of_added_invoices} invoices has been successfully added to the Database')



