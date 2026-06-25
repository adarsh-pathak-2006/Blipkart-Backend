from django.core.management.base import BaseCommand
from django.utils.text import slugify

from staff.models import Brands, Category, Products


class Command(BaseCommand):
    help = "Seed sample categories, brands, and products for local development."

    def handle(self, *args, **options):
        categories = [
            ("Mobiles", "Smartphones, feature phones, and mobile accessories"),
            ("Laptops", "Portable computers for work, study, and gaming"),
            ("Audio", "Headphones, earphones, speakers, and sound gear"),
            ("Home Appliances", "Useful appliances for everyday home use"),
            ("Fashion", "Clothing and accessories for daily wear"),
        ]

        brands = [
            "Apple",
            "Samsung",
            "Sony",
            "Dell",
            "Nike",
        ]

        products = [
            {
                "name": "iPhone 15",
                "description": "Flagship smartphone with A16 Bionic, advanced camera, and OLED display.",
                "price": 79999,
                "stock": 12,
                "category": "Mobiles",
                "brand": "Apple",
                "isactive": True,
            },
            {
                "name": "Galaxy S24",
                "description": "Premium Android phone with excellent display and camera performance.",
                "price": 74999,
                "stock": 15,
                "category": "Mobiles",
                "brand": "Samsung",
                "isactive": True,
            },
            {
                "name": "Sony WH-1000XM5",
                "description": "Noise-cancelling wireless headphones with balanced sound and long battery life.",
                "price": 29999,
                "stock": 25,
                "category": "Audio",
                "brand": "Sony",
                "isactive": True,
            },
            {
                "name": "Dell XPS 13",
                "description": "Slim productivity laptop with premium build and strong everyday performance.",
                "price": 119999,
                "stock": 8,
                "category": "Laptops",
                "brand": "Dell",
                "isactive": True,
            },
            {
                "name": "Nike Air Max",
                "description": "Comfortable lifestyle sneakers for everyday wear.",
                "price": 9999,
                "stock": 40,
                "category": "Fashion",
                "brand": "Nike",
                "isactive": True,
            },
            {
                "name": "Samsung Galaxy Buds",
                "description": "Compact true wireless earbuds with clear audio and charging case.",
                "price": 8999,
                "stock": 30,
                "category": "Audio",
                "brand": "Samsung",
                "isactive": True,
            },
            {
                "name": "Dell Inspiron 15",
                "description": "Reliable laptop for office work, study, and multitasking.",
                "price": 64999,
                "stock": 10,
                "category": "Laptops",
                "brand": "Dell",
                "isactive": True,
            },
            {
                "name": "Apple AirPods Pro",
                "description": "Wireless earbuds with active noise cancellation and spatial audio.",
                "price": 24999,
                "stock": 18,
                "category": "Audio",
                "brand": "Apple",
                "isactive": True,
            },
            {
                "name": "Smart LED TV",
                "description": "Compact smart television with streaming support and crisp display.",
                "price": 45999,
                "stock": 7,
                "category": "Home Appliances",
                "brand": "Samsung",
                "isactive": True,
            },
            {
                "name": "Running T-Shirt",
                "description": "Breathable sports t-shirt suitable for workouts and casual wear.",
                "price": 1499,
                "stock": 60,
                "category": "Fashion",
                "brand": "Nike",
                "isactive": True,
            },
        ]

        category_map = {}
        for name, description in categories:
            category, created = Category.objects.get_or_create(
                name=name,
                defaults={"description": description},
            )
            if not created and category.description != description:
                category.description = description
                category.save(update_fields=["description"])
            category_map[name] = category

        brand_map = {}
        for name in brands:
            brand, _ = Brands.objects.get_or_create(name=name)
            brand_map[name] = brand

        created_count = 0
        updated_count = 0

        for item in products:
            slug = slugify(item["name"])
            product, created = Products.objects.get_or_create(
                slug=slug,
                defaults={
                    "name": item["name"],
                    "description": item["description"],
                    "price": item["price"],
                    "stock": item["stock"],
                    "category": category_map[item["category"]],
                    "brand": brand_map[item["brand"]],
                    "isactive": item["isactive"],
                },
            )
            if created:
                created_count += 1
            else:
                product.name = item["name"]
                product.description = item["description"]
                product.price = item["price"]
                product.stock = item["stock"]
                product.category = category_map[item["category"]]
                product.brand = brand_map[item["brand"]]
                product.isactive = item["isactive"]
                product.save()
                updated_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Seeded {len(category_map)} categories, {len(brand_map)} brands, "
                f"{created_count} new products, {updated_count} updated products."
            )
        )
