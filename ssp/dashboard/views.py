from django.shortcuts import render
from . forms import *
from django.contrib imprt messages
from django.views import generic 

# Create your views here.

def home (request):
    return render(request,'dashboard/home.html')

def notes(request):
    if request.method == "POST":
        form=Notesform(request.POST)
        if form.is_valid():
            notes=Notes(user=request.user,title=request.POST['title'],description=request.POST['description'])
            notes.save()
        messages.sucess(request,f"NOtes Added from {request.user.username} Successfully..")
    else:
        form=Notesform()
    notes=Notes.objects.filter(user=request.user)
    context={'notes':notes,'form':form}
    return render(request,'dashboard/notes.html',context)


def delete_note(request,pk=None):
    NOtes.objects.get(id=pk).delete()
    return redirect ("notes")

class NOtesDetaailView(generic.Detailview):
    model =Notes

def homework (request):
    homework=Homework.objects.filter(user=request.user)
    context={'homeworks':homework}
    return render (request,'dashboard/homework.html')


