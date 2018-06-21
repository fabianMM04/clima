class FormMedicion(forms.ModelForm):
    class Meta:
        model = Medicion
        fields = ['temp', 'humedad', 'viento', 'desc']
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(FormConsig, self).__init__(*args, **kwargs)
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
        model = Consignacion
        fields = ['lat', 'lon']
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(FormConsig, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.form_method = 'post'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-5'
        self.fields['lat'].required = True
        self.fields['lon'].required = True
        self.helper.add_input(Submit('submit', 'Enviar'))
