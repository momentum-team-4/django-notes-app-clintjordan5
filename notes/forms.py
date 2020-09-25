from django.forms import ModelForm, Form, CharField, ChoiceField
from .models import Note


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = [
            'title',
            'body',
        ]

class NoteSearchForm(Form):
    SEARCH = [
    ("contains", "contains"),
    ("exact match", "exact match"),
    ]
    title = CharField()
    title_search_by = ChoiceField(choices=SEARCH)
    body = CharField()
    body_seafch_by = ChoiceField(choices=SEARCH)

