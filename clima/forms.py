'''
from crispy_forms.layout import Submit
from django import forms
from crispy_forms.helper import FormHelper
from .models import Medicion, Coordenadas, Sensor


class FormMedicion(forms.ModelForm):
    class Meta:
        model = Medicion
        fields = ['temp', 'humedad', 'viento', 'desc']
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(FormMedicion, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.form_method = 'post'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-5'
        self.fields['temp'].required = True
        self.fields['humedad'].required = True
        self.fields['viento'].required = True
        self.fields['desc'].required = True
        self.helper.add_input(Submit('submit', 'Enviar'))


class FormCoor(forms.ModelForm):
    class Meta:
        model = Coordenadas
        fields = ['lat', 'lon']
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(FormCoor, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.form_method = 'post'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-5'
        self.fields['lat'].required = True
        self.fields['lon'].required = True
        self.helper.add_input(Submit('submit', 'Enviar'))


class FormSensor(forms.ModelForm):
    class Meta:
        model = Sensor
        fields = ['tipo', 'est', 'medicion_id', 'coor_id']
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(FormConsig, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.form_method = 'post'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-5'
        self.fields['tip'].required = True
        self.fields['est'].required = True
        self.fields['medicion_id'].required = True
        self.fields['coor_id'].required = True
        self.helper.add_input(Submit('submit', 'Enviar'))
'''
