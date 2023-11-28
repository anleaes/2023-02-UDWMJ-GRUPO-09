from .forms import ArteForm
from .models import Arte
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
def add_arte(request):
    template_name = 'arte/add_arte.html'
    context = {}
    if request.method == 'POST':
        form = ArteForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('arte:list_arte')
    form = ArteForm()
    context['form'] = form
    return render(request, template_name, context)


def edit_arte(request, id_arte):
    template_name = 'arte/add_arte.html'
    context ={}
    arte = get_object_or_404(arte, id=id_arte)
    if request.method == 'POST':
        form = ArteForm(request.POST, instance=arte)
        if form.is_valid():
            form.save()
            return redirect('arte:list_arte')
    form = ArteForm(instance=arte)
    context['form'] = form
    return render(request, template_name, context)

def delete_arte(request, id_arte):
    arte= arte.objects.get(id=id_arte)
    arte.delete()
    return redirect('arte:list_arte') 

def list_arte(request):
    template_name = 'arte/list_arte.html'
    query = request.GET.get('query')
    
    
    clients = Arte.objects.filter()
    context = {
        'clients': clients,
        
    }
    return render(request,template_name, context)
 
