from django.shortcuts import render, redirect
from django.contrib.messages import success
from .data import NOTES
from .models import Note
from .forms import NoteForm, NoteSearchForm

def notes_list(request):
     return render(request, "notes/notes_list.html", {"notes": NOTES})

def notes_detail(request, pk):
    note = NOTES[pk]
    return render(request, "notes/notes_detail.html", {"note": NOTES})

def notes_create(request):
    if request.method == "GET":
        form = NoteForm()
    else:
        form = NoteForm(data=request.POST)
        if form.is_valid():
            form.save()
            success(request, "note created")
            return redirect(to='notes_list')
    return render(request, 'notes/notes_create.html', {'form': form})



# Create your views here.
