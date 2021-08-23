from django import forms 
from .models import *


class CommentForm(forms.Form):
   body = forms.CharField(label="",widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Text Goes Here !"
        })
    )

''' class CommentForm(forms.Form):
   body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )
   '''
