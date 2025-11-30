from django.shortcuts import render
from .products_data import products

# Homepage: latest + best sellers
def home_products(request):
    latest = sorted(products, key=lambda p: p["id"])[:10]
    best_sellers = [p for p in products if p.get("bestseller")][:5]
    context = {"latest": latest, "best_sellers": best_sellers}
    return render(request, "home_products.html", context)

# Products page
def index(request):
    return render(request, "index.html")

# Optional: about page
def about(request):
    return render(request, "about.html")

# Optional: contact page
def contact(request):
    return render(request, "contact.html")
