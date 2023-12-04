from .forms import ClienteForm
from .models import Cliente
from django.shortcuts import render, get_object_or_404, redirect

def add_cliente(request):
    template_name = 'clientes/add_cliente.html'
    context = {}
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('clientes:list_clientes')
    form = ClienteForm()
    context['form'] = form
    return render(request, template_name, context)

def list_clientes(request):
    template_name = 'clientes/list_clientes.html'
    clientes = Cliente.objects.filter()
    context = {
        'clientes': clientes,
    }
    return render(request,template_name, context)


def edit_cliente(request, id_clientes):
    template_name = 'clientes/add_cliente.html'
    context ={}
    clientes= get_object_or_404(Cliente, id=id_clientes)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=clientes)
        if form.is_valid():
            form.save()
            return redirect('clientes:list_clientes')
    form = ClienteForm(instance=clientes)
    context['form'] = form
    return render(request, template_name, context)

def delete_cliente(request, id_cliente):
    cliente = Cliente.objects.get(id=id_cliente)
    cliente.delete()
    return redirect('clientes:list_clientes')

def search_clientes(request):
    template_name = 'clientes/list_clientes.html'
    query = request.GET.get('query')
    clientes = Cliente.objects.filter(name=query)
    context = {
        'clientes': clientes,
    } 
    return render(request,template_name, context)
