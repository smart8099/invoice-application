from faker import Faker
import csv

fake = Faker()


def generate_invoices():
    expiration_date = fake.future_date()
    invoice_items_count = fake.random_int(0,500)
    recipient_name = fake.name()
    description = fake.text()

    return [expiration_date, invoice_items_count, recipient_name,description]


with open('another_sample_invoices.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Expiration Date', 'Number of Invoices', 'Recipient Name', 'Description'])
    for n in range(1, 100000):
        writer.writerow(generate_invoices())

