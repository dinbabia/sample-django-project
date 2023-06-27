from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProductForm, RawProductForm
# Create your views here.
from .models import Product

# def product_create_view(request, *args, **kwargs):
#     '''Render initial data
#     with the use of obj->Product.objects.get(id=1),
#     we can make this as an Update page....''' 
#     initial_data = {
#         "title" : "Initial Title in product Create "
#     }
#     obj = Product.objects.get(id=1)
#     form = ProductForm(request.POST or None, initial=initial_data, instance=obj)
#     context = {
#         "form" : form
#     }
#     if form.is_valid():
#         form.save()
#     return render(request, "products/product_create.html", context)

# def product_create_view(request):
#     raw_form = RawProductForm()
#     if request.method == "POST":
#         raw_form = RawProductForm(request.POST)
#         if raw_form.is_valid():
#             print(raw_form.cleaned_data)
#     context = {
#         "form" : raw_form
#     }
#     return render(request, "products/product_create.html", context)


def product_create_view(request):
    '''ORIGINAL PRODUCT CREATE VIEW''' 
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form' : form
    }
    return render(request, "products/product_create.html", context)


def product_update_view(request, id=id):
    '''ORIGINAL PRODUCT UPDATE VIEW'''
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form' : form
    }
    return render(request, "products/product_create.html", context)

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list" : queryset
    }
    return render(request, "products/product_list.html", context)


def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        # Confirm Delete
        obj.delete()
        return redirect("/")
    context = {
        "obj" : obj
    }
    return render(request, "products/product_delete.html", context)

def product_detail_view(request, id):
    '''With dynamic url routing'''
    # obj = Product.objects.get(id=id)
    obj = get_object_or_404(Product, id=id)
    context = {
        "object" : obj
    }
    return render(request, "products/product_detail.html", context)

# def product_detail_view(request):
#     '''This is old implementation without dynamic url routing'''
#     obj = Product.objects.get(id=1)
#     context = {
#         "object" : obj
#     }
#     return render(request, "products/product_detail.html", context)
