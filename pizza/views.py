from django.forms import formset_factory
from django.shortcuts import render
from .forms import PizzaForm,MultiplePizzaForm
def home(request):
    return render(request,'pizza/home.html')

def order(request):
    mulform= MultiplePizzaForm()
    if request.method=='POST':
        form_data=PizzaForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            note=f"Thanks for ordering! Your {form_data.cleaned_data['size']} pizz is on its way"
            form= PizzaForm()
            return render(request,'pizza/order.html',{'form':form,'note':note,'mulform':mulform})


    else:
        mulform= MultiplePizzaForm()
        form= PizzaForm()
        print(mulform)
        return render(request,'pizza/order.html',{'form':form,'mulform':mulform})


def pizzas(request):
    num_of_pizzas=2
    form= MultiplePizzaForm(request.GET)
    if form.is_valid():
        num_of_pizzas=form.cleaned_data['numbers']
    pizzaformset=formset_factory(PizzaForm,extra=num_of_pizzas)
    formset=pizzaformset()
    if request.method=='POST':
        
        filled_pizza_forms=pizzaformset(request.POST)
        if filled_pizza_forms.is_valid():
            for form in filled_pizza_forms:
                print(form.cleaned_data['size'])
            note='Pizzas have been ordered'
        else:
            note='try again'
        return render(request,'pizza/pizzas.html',{'note':note,'formset':formset})
    else:
        return render(request,'pizza/pizzas.html',{'formset':formset})