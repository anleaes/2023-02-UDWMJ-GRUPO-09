from .forms import CompraForm
from .models import Compra
from django.shortcuts import render, get_object_or_404, redirect

def add_compra(request):
    template_name = 'compras/add_compra.html'
    context = {}
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('compras:list_compras')
    form = CompraForm()
    context['form'] = form
    return render(request, template_name, context)

def list_compras(request):
    template_name = 'compras/list_compras.html'
    compras = Compra.objects.filter()
    context = {
        'compras': compras,
    }
    return render(request,template_name, context)


def edit_compra(request, id_compras):
    template_name = 'compras/add_compra.html'
    context ={}
    compras= get_object_or_404(Compra, id=id_compras)
    if request.method == 'POST':
        form = CompraForm(request.POST, instance=compras)
        if form.is_valid():
            form.save()
            return redirect('compras:list_compras')
    form = CompraForm(instance=compras)
    context['form'] = form
    return render(request, template_name, context)

def delete_compra(request, id_compra):
    compra = Compra.objects.get(id=id_compra)
    compra.delete()
    return redirect('compras:list_compras')

def search_compras(request):
    template_name = 'compras/list_compras.html'
    query = request.GET.get('query')
    compras = Compra.objects.filter(name=query)
    context = {
        'compras': compras,
    } 
    return render(request,template_name, context)