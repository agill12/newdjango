from django import forms
from .models import Message

class ComposeForm(forms.ModelForm):
    
    class Meta:
        model=Message
        fields=('subject','body','sender','recipient','read')
    