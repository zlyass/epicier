from django.shortcuts import render, redirect  
from clients.forms import ClientForm
from clients.models import Client
from credits.models import Credit
from django.db.models import Sum
# Create your views here.
def clients(request):  
    if request.method == "POST":  
        form = ClientForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/clients/show')  
            except:  
                pass  
    else:  
        form = ClientForm()  
   
    return render(request,'index.html',{'form':form,"pageClient":"active"})  
def show(request):  
    clients = Client.objects.all()  
    return render(request,"show.html",{'clients':clients,"pageClient":"active"})  
def search(request):  
    name=request.GET.get('name')
    clients = Client.objects.filter(name__contains=name,) 
    return render(request,"show.html",{'clients':clients,"pageClient":"active"})  
def edit(request, id):  
    client = Client.objects.get(id=id)  
    return render(request,'edit.html', {'client':client,"pageClient":"active"})  
def update(request, id):  
    client = Client.objects.get(id=id)  
    form = ClientForm(request.POST, instance = client)  
    if form.is_valid():  
        form.save()  
        return redirect("/clients/show")  
    return render(request, 'edit.html', {'client': client,"pageClient":"active"})  
def destroy(request, id):  
    client = Client.objects.get(id=id)  
    client.delete()  
    return redirect("/clients/show")