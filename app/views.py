from django.shortcuts import render, redirect
from app.forms import UsuarioForm
from app.models import Usuario
from django.core.paginator import Paginator

# Views de cada função

def home(request):
    data = {}
    all = Usuario.objects.all()
    paginator = Paginator(all, 3    )
    pages = request.GET.get('page')
    data['db'] = paginator.get_page(pages)
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data ['form'] = UsuarioForm()
    return render(request, 'form.html', data)

def create(request):
    form = UsuarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Usuario.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Usuario.objects.get(pk=pk)
    data['form'] = UsuarioForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Usuario.objects.get(pk=pk)
    form = UsuarioForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request,pk):
    db = Usuario.objects.get(pk=pk)
    db.delete()
    return redirect('home')