from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Chicken, Toy
from .forms import FeedingForm

class ChickenCreate(CreateView):
    model = Chicken
    fields = ['name', 'breed', 'description', 'age']

class ChickenUpdate(UpdateView):
    model = Chicken
    fields = ['breed', 'description', 'age']

class ChickenDelete(DeleteView):
    model = Chicken
    success_url = '/chickens/'

def home (request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def chickens_index(request):
    chickens = Chicken.objects.all()
    return render(request, 'chickens/index.html', {'chickens': chickens})

def chickens_detail(request, chicken_id):
    chicken = Chicken.objects.get(id=chicken_id)
    toys_chicken_doesnt_have = Toy.objects.exclude(id__in = chicken.toys.all().values_list('id'))
    feeding_form = FeedingForm()
    return render(request, 'chickens/detail.html', {
        'chicken': chicken, 'feeding_form': feeding_form,
        'toys': toys_chicken_doesnt_have
        })

def add_feeding(request, chicken_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.chicken_id = chicken_id
        new_feeding.save()
    return redirect('detail', chicken_id=chicken_id)

def assoc_toy(request, chicken_id, toy_id):
    Chicken.objects.get(id=chicken_id).toys.add(toy_id)
    return redirect('detail', chicken_id=chicken_id)

def unassoc_toy(request, chicken_id, toy_id):
    Chicken.objects.get(id=chicken_id).toys.remove(toy_id)
    return redirect('detail', chicken_id=chicken_id)

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'