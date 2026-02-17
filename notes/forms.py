from django import forms
from .models import Note


class NoteForm(forms.Form):
    title = forms.CharField(max_length=100,
                            error_messages={
                                'required': 'Title is required.'}
                            )
    description = forms.CharField(widget=forms.Textarea(),
                                  error_messages={
                                      'required': 'Please enter a description.'}
                                  )

    def create(self, validated_data):
        return Note.objects.create(**validated_data)
