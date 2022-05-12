from django import forms

class CursoForm (forms.Form):

    curso = forms.CharField()
    comision = forms.IntegerField()