from django.shortcuts import render, redirect
from main.models import Product
from main.forms import ProductForm

def show_main(request):
    product_entries = Product.objects.all()
    context = {
        'app_name': 'THRIFTxYouth',
        'name': 'Abhiseka Susanto',
        'class': 'C',
        'npm': '2306244942',
        'product_entries': product_entries
    }
    return render(request, "main.html", context)

def create_product_entry(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)
