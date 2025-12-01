import csv
import os
from django.conf import settings
from django.core.management.base import BaseCommand
from Users.models import Product

class Command(BaseCommand):
    help = "Import products from CSV"

    def handle(self, *args, **kwargs):
        # Correct path to your CSV
        csv_path = os.path.join(settings.BASE_DIR, "Users", "data", "products.csv")

        with open(csv_path, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                Product.objects.update_or_create(
                    id=row["id"],
                    defaults={
                        "name": row["name"],
                        "image": row["image"],
                        "price": row["price"],
                        "description": row["description"],
                        "category": row["category"],
                        "type": row["type"],
                        "bestseller": row["bestseller"].lower() == "true",
                    }
                )
        self.stdout.write(self.style.SUCCESS("Products imported successfully!"))
