from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template import loader
from .models import Tracker
from .forms import TrackerForm

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def index(request):
    items = Tracker.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'items': items,
    }
    return HttpResponse(template.render(context, request))

def create(request):
    context = {}
    form = TrackerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    
    context['form'] = form
    template = loader.get_template('create.html')
    return HttpResponse(template.render(context, request))

def detail(request, id):
    data = Tracker.objects.get(id = id)
    template = loader.get_template('detail.html')
    context = {
        'data': data,
    }
    return HttpResponse(template.render(context, request))

def update(request, id):
    context = {}
    data = get_object_or_404(Tracker, id = id)
    form = TrackerForm(request.POST or None, instance = data)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + str(id))
    
    context['form'] = form
    template = loader.get_template('create.html')
    return HttpResponse(template.render(context, request))

def destroy(request, id):
    data = get_object_or_404(Tracker, id = id)
    data.delete()
    return HttpResponseRedirect("/")

def search(request):
    items = Tracker.objects.all().values_list('category', flat=True).distinct()
    template = loader.get_template('search.html')
    context = {
        'items': items,
    }
    return HttpResponse(template.render(context, request))

def filter(request):
    search_cat = request.POST['category']
    items = Tracker.objects.filter(category=search_cat).values()
    template = loader.get_template('result.html')
    context = {
        'items': items,
    }
    return HttpResponse(template.render(context, request))

def report(request):
    template = loader.get_template('report.html')
    return HttpResponse(template.render())