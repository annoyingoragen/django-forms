from django.shortcuts import render
from .forms import PizzaForm
def home(request):
    return render(request,'pizza/home.html')

def order(request):
    if request.method=='POST':
        form_data=PizzaForm(request.POST)
        if form_data.is_valid():
            note=f"Thanks for ordering! Your {form_data.cleaned_data['size']} pizz is on its way"
            form= PizzaForm()
            return render(request,'pizza/order.html',{'form':form,'note':note})


    else:
        form= PizzaForm()
        return render(request,'pizza/order.html',{'form':form})
