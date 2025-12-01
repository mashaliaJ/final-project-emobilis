from django.shortcuts import render
from .models import Product

def home_products(request):
    latest = Product.objects.order_by('-id')[:10]
    best_sellers = Product.objects.filter(bestseller=True)[:5]
    context = {"latest": latest, "best_sellers": best_sellers}
    return render(request, "home_products.html", context)

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def collections(request):
    products = Product.objects.all()
    
    # Filter by category
    selected_categories = request.GET.getlist('category')
    if selected_categories:
        products = products.filter(category__in=selected_categories)
    
    # Sorting
    sort_option = request.GET.get('sort')
    if sort_option == 'price_asc':
        products = products.order_by('price')
    elif sort_option == 'price_desc':
        products = products.order_by('-price')
    elif sort_option == 'name_asc':
        products = products.order_by('name')
    elif sort_option == 'name_desc':
        products = products.order_by('-name')

    # Get all unique categories for filter checkboxes
    categories = Product.objects.values_list('category', flat=True).distinct()

    context = {
        "products": products,
        "categories": categories,
        "selected_categories": selected_categories,
        "sort_option": sort_option,
    }
    return render(request, "collections.html", context)

# Product detail page
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    context = {
        "product": product
    }
    return render(request, "product_detail.html", context)
