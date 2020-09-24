from django.shortcuts import render
from .data import NOTES

def notes_list(request):
     return render(request, "notes/notes_list.html", {"notes": NOTES})

def notes_detail(request, pk):
    note = NOTES[pk]
    return render(request, "notes/notes_detail.html", {"notes": NOTES})

# Create your views here.
