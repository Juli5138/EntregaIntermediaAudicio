from django import forms
 
class AutorFormulario(forms.Form):
    autor = forms.CharField()
    info = forms.IntegerField()
    orden=forms.IntegerField()
