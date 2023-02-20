from django.shortcuts import redirect, render
from clients.models import Client
from credits.models import Credit
from django.db.models import Sum
# Create your views here.
def show(request):
    if request.user.is_authenticated:
        user=request.user
        clients=Client.objects.all()
        #credits = Credit.objects.all()  
        totalCredits=Credit.objects.all().aggregate(Sum('total'))
        totalCreditsPaye=Credit.objects.filter(etat=True).aggregate(Sum('total'))
        clientAvecCredit=Credit.objects.filter(etat=False).values_list('client').distinct()
        tauxCreditsPaye=0
        creditNonPaye=0
        total=0
        if totalCredits['total__sum']:
            total=totalCredits['total__sum']
            creditNonPaye=totalCredits['total__sum']-totalCreditsPaye['total__sum']
            tauxCreditsPaye=round(totalCreditsPaye['total__sum']/totalCredits['total__sum']*100,2)
        return render(request,"profile.html",
                      {
                        'user':user,
                        'nbrClient':len(clients),
                        'nbrClientSansCredit':len(clients)-len(clientAvecCredit),
                        'totalCredits':total,
                        'tauxCreditsPaye':tauxCreditsPaye,
                        'creditNonPaye':creditNonPaye,
                        'nbrClientAvecCredit':len(clientAvecCredit),
                        'home':'active'
                      }
                    ) 
    else:  
        return redirect('/accounts/login')
    