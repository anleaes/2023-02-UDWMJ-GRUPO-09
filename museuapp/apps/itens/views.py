from .forms import ItemForm
from .models import Item
from django.shortcuts import render, get_object_or_404, redirect

def add_item(request):
    template_name = 'itens/add_item.html'
    context = {}
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('itens:list_itens')
    form = ItemForm()
    context['form'] = form
    return render(request, template_name, context)

def list_itens(request):
    template_name = 'itens/list_itens.html'
    itens = Item.objects.filter()
    context = {
        'itens': itens,
    }
    return render(request,template_name, context)


def edit_item(request, id_itens):
    template_name = 'itens/add_item.html'
    context ={}
    itens= get_object_or_404(Item, id=id_itens)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=itens)
        if form.is_valid():
            form.save()
            return redirect('itens:list_itens')
    form = ItemForm(instance=itens)
    context['form'] = form
    return render(request, template_name, context)

def delete_item(request, id_item):
    item = Item.objects.get(id=id_item)
    item.delete()
    return redirect('itens:list_itens')

def search_itens(request):
    template_name = 'itens/list_itens.html'
    query = request.GET.get('query')
    itens = Item.objects.filter(name=query)
    context = {
        'itens': itens,
    } 
    return render(request,template_name, context)