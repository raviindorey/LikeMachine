from django import forms

from .models import LinkPost


class LinkPostForm(forms.ModelForm):
    class Meta:
        model = LinkPost
        fields = ('title', 'link')
