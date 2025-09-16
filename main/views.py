from django.shortcuts import render
from .models import Product

def show_main(request):
    Product.objects.create(
        name="Cristiano Ronaldo FunkoPop",
        price=500000,
        description="Limited edition FunkoPop of CR7 in Portugal kit",
        thumbnail="https://i5.walmartimages.com/asr/5ed3bec2-9e53-40ac-897b-0f065a480f1f.1a8e834e36c383de62d9b8483c92cae1.png",
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
