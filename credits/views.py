from django.shortcuts import render, redirect
from clients.models import Client  
from credits.forms import CreditForm
from credits.models import Credit
from products.models import Product

# Create your views here.
def credits(request): 
    print("run credit view ") 
    if request.method == "POST":  
        form = CreditForm(request.POST)  
        formcopy = CreditForm(request.POST.copy())
        formcopy.data["price"]=Product.objects.get(id=formcopy.data["product"]).selling_price
        formcopy.data["total"]=formcopy.data["price"]*float(formcopy.data["quantite"])
        if formcopy.is_valid():
            try:  
                formcopy.save()  
                return redirect('/credits/show')  
            except Exception as e:  
                print(e)
        else:
            print(form.errors)      

    else:  
        form = CreditForm() 
    products=Product.objects.all()
    clients=Client.objects.all() 
    return render(request,'credit_index.html',{'form':form,'products':products,'clients':clients,"pageCredit":"active"})  
def show(request):  
    credits = Credit.objects.all()  
    clients=Client.objects.all() 
    return render(request,"credit_show.html",{'credits':credits,"pageCredit":"active","clients":clients})  

def getCreditClientid(request,id):  
    clients=Client.objects.all()
    client=Client.objects.get(id=id)
    credits = Credit.objects.filter(client_id=id)
    return render(request,"credit_show.html",{'credits':credits,"pageCredit":"active","clients":clients,"sClient":client})
def edit(request, id):  
    products=Product.objects.all()
    clients=Client.objects.all() 
    credit = Credit.objects.get(id=id)  
    return render(request,'credit_edit.html', {'credit':credit,'products':products,'clients':clients,"pageCredit":"active"})  
def update(request, id):  
    credit = Credit.objects.get(id=id)   
    formcopy = CreditForm(request.POST.copy(),instance = credit)
    formcopy.data["price"]=Product.objects.get(id=formcopy.data["product"]).price
    formcopy.data["total"]=formcopy.data["price"]*float(formcopy.data["quantite"])
    if formcopy.is_valid():  
        formcopy.save()  
        return redirect("/credits/show")  
    return render(request, 'credit_edit.html', {'credit': credit,"pageCredit":"active"})  
def destroy(request, id):  
    credit = Credit.objects.get(id=id)  
    credit.delete()  
    return redirect("/credits/show")
def paye(request, id):  
    credit = Credit.objects.get(id=id)  
    credit.etat=True
    credit.save()
    return redirect("/credits/show")