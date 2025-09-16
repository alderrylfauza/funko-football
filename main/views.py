from django.shortcuts import render
from .models import Product

def show_main(request):
    Product.objects.create(
        name="Cristiano Ronaldo FunkoPop",
        price=500000,
        description="Limited edition FunkoPop of CR7 in Portugal kit",
        thumbnail="https://example.com/cr7.jpg",
        category="Football Player",
        stock=10,
        is_featured=True
    )

    products = Product.objects.all()
    context = {
        "app_name": "Football FunkoPop Shop",
        "class_name": "PBP D",
        "products": products,
    }
    return render(request, "main.html", context)
