from django import forms


class EditArcicle(forms.Form):
    title = forms.CharField(max_length=50)
    content = forms.DateField()

class SearchArticle(forms.Form):
    title = forms.CharField(max_length=50)