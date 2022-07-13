from django import forms

class MozoFormulario(forms.Form):
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    antiguedad=forms.DateField()
    fechaDeNacimiento=forms.DateField()

class CocineroFormulario(forms.Form):
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    antiguedad=forms.DateField()
    fechaDeNacimiento=forms.DateField()

class LavaplatosFormulario(forms.Form):
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    antiguedad=forms.DateField()
    fechaDeNacimiento=forms.DateField()

