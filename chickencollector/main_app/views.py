from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Chicken
from .forms import FeedingForm

class ChickenCreate(CreateView):
    model = Chicken
    fields = '__all__'

class ChickenUpdate(UpdateView):
    model = Chicken
    fields = ['name', 'breed', 'description', 'age']

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
    feeding_form = FeedingForm()
    return render(request, 'chickens/detail.html', {'chicken': chicken, 'feeding_form': feeding_form})

def add_feeding(request, chicken_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.chicken_id = chicken_id
        new_feeding.save()
    return redirect('detail', chicken_id=chicken_id)