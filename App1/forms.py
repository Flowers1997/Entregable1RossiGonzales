from django import forms

class MozoFormulario(forms.Form):
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    antiguedad=forms.DateField(default="2022-11-22")
    fechaDeNacimiento=forms.DateField(default="2022-11-22")

class CocineroFormulario(forms.Form):
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    antiguedad=forms.DateField(default="2022-11-22")
    fechaDeNacimiento=forms.DateField(default="2022-11-22")

class LavaplatosFormulario(forms.Form):
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    antiguedad=forms.DateField(default="2022-11-22")
    fechaDeNacimiento=forms.DateField(default="2022-11-22")

