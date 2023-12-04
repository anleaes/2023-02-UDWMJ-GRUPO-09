from .forms import EntidadeForm
from .models import Entidade
from django.shortcuts import render, get_object_or_404, redirect

def add_entidade(request):
    template_name = 'entidades/add_entidade.html'
    context = {}
    if request.method == 'POST':
        form = EntidadeForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('entidades:list_entidades')
    form = EntidadeForm()
    context['form'] = form
    return render(request, template_name, context)

def list_entidades(request):
    template_name = 'entidades/list_entidades.html'
    entidade = Entidade.objects.filter()
    context = {
        'entidades': entidade,
    }
    return render(request,template_name, context)


def edit_entidade(request, id_entidades):
    template_name = 'entidades/add_entidade.html'
    context ={}
    entidades = get_object_or_404(Entidade, id=id_entidades)
    if request.method == 'POST':
        form = EntidadeForm(request.POST, instance=entidades)
        if form.is_valid():
            form.save()
            return redirect('entidades:list_entidades')
    form = EntidadeForm(instance=entidades)
    context['form'] = form
    return render(request, template_name, context)

def delete_entidade(request, id_entidade):
    entidade = Entidade.objects.get(id=id_entidade)
    entidade.delete()
    return redirect('entidades:list_entidades')

def search_artes(request):
    template_name = 'entidades/list_entidades.html'
    query = request.GET.get('query')
    entidades = Entidade.objects.filter(name=query)
    context = {
        'entidade': entidades,
    } 
    return render(request,template_name, context)