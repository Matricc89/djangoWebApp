from django import forms

class ClienteFormulario(forms.Form):

     nombre = forms.CharField()
     apellido = forms.CharField()
     edad = forms.IntegerField()


class SucursalFormulario(forms.Form):

     nombre = forms.CharField()
     direccion = forms.CharField()
     


class AutoFormulario(forms.Form):

     marca = forms.CharField()
     modelo = forms.CharField()
     color = forms.CharField()
     precio = forms.IntegerField()

class BuscarFormulario(forms.Form):
     marca = forms.CharField()