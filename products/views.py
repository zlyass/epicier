from django.shortcuts import render, redirect  
from products.forms import ProductForm
from products.models import Product

# Create your views here.
def products(request):  
    if request.method == "POST":  
        form = ProductForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/product/show')  
            except:  
                pass  
    else:  
        form = ProductForm()  
    return render(request,'product_index.html',{'form':form,"pageProduct":"active"})  
def show(request):  
    products = Product.objects.all()  
    return render(request,"product_show.html",{'products':products,"pageProduct":"active"})  

def search(request):
    name=request.GET.get('name')
    products = Product.objects.filter(name__contains=name,)
    return render(request,"product_show.html",{'products':products,"pageProduct":"active"})  
def edit(request, id):  
    product = Product.objects.get(id=id)  
    return render(request,'product_edit.html', {'product':product,"pageProduct":"active"})  
def update(request, id):  
    product = Product.objects.get(id=id)  
    form = ProductForm(request.POST, instance = product)  
    if form.is_valid():  
        form.save()  
        return redirect("/product/show")  
    return render(request, 'product_edit.html', {'product': product,"pageProduct":"active"})  
def destroy(request, id):  
    product = Product.objects.get(id=id)  
    product.delete()  
    return redirect("/product/show")