from django.shortcuts import render,redirect
from .forms import CalculationForm
from .models import Calculation


# Create your views here.
# functions

def index(request):
    if request.method=='POST':
        form = CalculationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.result = instance.principal*(instance.rate/100)*instance.time
            instance.save()
            return redirect('index')
    else:
        form = CalculationForm()
    calculations = Calculation.objects.all().order_by('timestamp')

    return render(request,'index.html',{'form':form,'calculations':calculations})

def delete_calculation(request, calculation_id):
    if request.method == 'POST':
        calculation = Calculation.objects.get(pk=calculation_id)
        calculation.delete()
        return redirect('calculation_list')  # Redirect to the page displaying calculations
    else:
        return redirect('calculation_list')  # Handle GET requests or invalid requests
    



    