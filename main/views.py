from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from .models import Product
from django.http import HttpResponse
from django.core import serializers

def show_main(request):
    products = Product.objects.all()
    context = {
        "app_name": "Football FunkoPop Shop",
        "class_name": "PBP D",
        "products": products,
        "username": "Alderryl Juan Fauza",
    }
    
    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect("main:show_main")
    context = {"form": form}
    return render (request, "create_product.html", context)

def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    context = {"product": product}
    return render (request, "product_detail.html", context)
    
def show_xml(request):
    data = Product.objects.all()
    xml_data = serializers.serialize("xml", data)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    json_data = serializers.serialize("json", data)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    xml_data = serializers.serialize("xml", data)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    json_data = serializers.serialize("json", data)
    return HttpResponse(json_data, content_type="application/json")