from django import forms
from .models import Files

class FileForm(forms.ModelForm):
    file = forms.FileField(required=True)
    
    class Meta:
        model = Files
        fields = ['nombre', 'file']

    def __init__(self, *args, **kwargs):
        super(FileForm, self).__init__(*args, **kwargs)
        # Agrega la clase de Bootstrap 'form-control' a cada campo
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        
        # Agrega placeholders específicos a los campos
        self.fields['nombre'].widget.attrs['placeholder'] = 'Nombre: '
        