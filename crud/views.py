from django.shortcuts import render, redirect
from .models import motif

# Create method


def add(request):

    return render(request, 'add.html')


def create(request):
    if request.method == "POST":
        nom = request.POST['nom']
        motif_Img = request.FILES['motif_Img']
        print(motif_Img.name)
        print(motif_Img.size)
        description = request.POST['description']
        id = None
        obj = motif(id, nom, motif_Img, description)
        obj.save()
        return redirect('/')

# Read method


def read(request):
    try:
        obj = motif.objects.all()
    except motif.DoesNotExist:
        obj = None
    return render(request, 'index.html', {'motifs': obj})

# Update method


def update(request, id):
    if request.method == "POST":
        nom = request.POST['nom']
        description = request.POST['description']
        motif_Img = request.FILES['motif_Img']
        obj1 = motif.objects.get(id=id)
        obj1.nom = nom
        obj1.description = description
        obj1.motif_Img = motif_Img
        obj1.save()
        return redirect('/')
    else:
        try:
            obj = motif.objects.get(id=id)
        except motif.DoesNotExist:
            obj = None

        return render(request, 'edit.html', {'motif': obj})

# Delete method


def delete(request, id):
    try:
        obj = motif.objects.get(id=id)
    except motif.DoesNotExist:
        obj = None

    obj.delete()
    return redirect('/')
