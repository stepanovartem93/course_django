from django.core.management.base import BaseCommand
from mainapp.models import ProductCategory, Product
from django.contrib.auth.models import User

import json, os

JSON_PATH = 'mainapp/json'

def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r' ) as infile:
        return json.load(infile)

class Command(BaseCommand):
    def handle(sself, *args, **options):
        categories = load_from_json('categories')

        ProductCategory.objects.all().delete()
        for category in categories:
            new_category = ProductCategory(**category)
            new_category.save()

            products = load_from_json('products')

            Product.objects.all().delete()
            for product in products:
                category_name = product["category"]
                