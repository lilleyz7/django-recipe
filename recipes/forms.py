from django import forms

class RecipeForm(forms.Form):
    name = forms.CharField(max_length=100)
    ingredients = forms.CharField(widget=forms.Textarea)
    steps = forms.CharField(widget=forms.Textarea)