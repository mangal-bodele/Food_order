from django.shortcuts import render,redirect
from .forms import FoodOrderForm
from .models import FoodOrder
from django.contrib.auth.decorators import login_required
@login_required(login_url='login_url')
def create_foodorder(request):
    template_name = 'crud_app/create.html'
    form = FoodOrderForm()
    if request.method =="POST":
        form = FoodOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form':form}
    return render(request, template_name, context)

@login_required(login_url='login_url')
def show_foodorder(request):
    template_name = 'crud_app/show.html'
    foodorders =FoodOrder.objects.all()
    context = {'foodorders': foodorders}
    return render(request, template_name, context)


def update_foodorder(request, pk):
    template_name = 'crud_app/create.html'
    obj = FoodOrder.objects.get(id=pk)
    form = FoodOrderForm(instance=obj)
    if request.method == "POST":
        form = FoodOrderForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)

def cancel_foodorder(request, pk):
    template_name = 'crud_app/confirm.html'
    obj = FoodOrder.objects.get(id=pk)
    if request.method == "POST":
        obj.delete()
        return redirect('show_url')
    return render(request, template_name)
