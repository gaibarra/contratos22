from django import forms
from django.contrib.auth.models import User 
from .models import Departamento, Partes, Contratos, Puestos





class DepartamentoForm(forms.ModelForm):
    class Meta:
        model=Departamento
        fields=['claveDepartamento','claveCampus','claveArea','nombreDepartamento','f001', 'f002','f003', 'testigoUsual1', 'testigoUsual2','estado']
        exclude = ['um','fm','uc','fc']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

        self.fields['nombreDepartamento'].widget.attrs['style'] = "width:400px"
        self.fields['testigoUsual1'].widget.attrs['style'] = "width:400px"
        self.fields['testigoUsual2'].widget.attrs['style'] = "width:400px"
        self.fields['f001'].widget.attrs['style'] = "width:400px"
        self.fields['f002'].widget.attrs['style'] = "width:400px"
        self.fields['f003'].widget.attrs['style'] = "width:400px"

class PartesForm(forms.ModelForm):
        
    
    claveDepartamento = forms.ModelChoiceField(
        queryset=Departamento.objects.filter(estado=True)
            .order_by('claveDepartamento')
        )
    
    domicilioParte = forms.CharField(
            widget=forms.Textarea(
                attrs={
                    "rows": 3,
                    "cols": 80,
                    "placeholder": "Domicilio completo",
                    "verbose_name": "Domicilio",
                    }
                )
            )
    class Meta:
        model =Partes
        fields=['claveDepartamento', 'estatusParte', 'codigo', 'tituloParte', 'nombresParte', 'apellidoPaternoParte', 'apellidoMaternoParte','fecha_ingreso', 'email', 'lugarnacimientoParte', 'rfc', 'imss',  'curp', 'nacionalidadParte','estadocivilParte','regfiscalParte', 'cedula_profParte', 'titulo_profParte', 'universidadParte','domicilioParte', 'phone', 'mobile','grupo_sanguineo','alergias','clavePuesto','actividadesParte']
        exclude = ['um','fm','uc','fc']
    
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

        self.fields['estatusParte'].widget.attrs['style'] = "width:450px"
        self.fields['codigo'].widget.attrs['style'] = "width:100px"
        self.fields['codigo'].widget.attrs['readonly'] = True
        self.fields['claveDepartamento'].widget.attrs['style'] = "width:540px"
        self.fields['tituloParte'].widget.attrs['style'] = "width:110px"
        self.fields['apellidoPaternoParte'].widget.attrs['style'] = "width:160px"
        self.fields['apellidoMaternoParte'].widget.attrs['style'] = "width:160px"
        self.fields['titulo_profParte'].widget.attrs['style'] = "width:300px"
        self.fields['universidadParte'].widget.attrs['style'] = "width:400px"  
        self.fields['cedula_profParte'].widget.attrs['style'] = "width:200px"
        self.fields['clavePuesto'].widget.attrs['style'] = "width:500px"
        self.fields['clavePuesto'].widget.attrs['verbose_name'] = "Puesto"
        self.fields['domicilioParte'].widget.attrs['verbose_name'] = "Domicilio"
        self.fields['actividadesParte'].widget.attrs['style'] = "width:600px"
class ContratosForm(forms.ModelForm):
    
    datecontrato = forms.DateField(
            label= "Fecha del Contrato",
             
            widget=forms.DateInput(
                format='%Y-%m-%d',
                
                attrs={
                    'style': 'text-right',
                    }
                )
            )
    datecontrato_ini = forms.DateField(
            label= "Fecha inicial",
             
            widget=forms.DateInput(
                format='%Y-%m-%d',
                
                attrs={
                    'style': 'text-right',
                    }
                )
            )
    datecontrato_fin = forms.DateField(
            label= "Fecha final ",
             
            widget=forms.DateInput(
                format='%Y-%m-%d',
                
                attrs={
                    'style': 'text-right',
                    }
                )
            )                        
    class Meta:
        model=Contratos
        fields=['id', 'tipocontrato','datecontrato','parte2' , 'datecontrato_ini', 'datecontrato_fin', 'importeContrato', 'status', 'npContrato', 'imppContrato', 'totalhorasContrato',
        'testigoContrato1',  'testigoContrato2']
        exclude = ['um','fm','uc','fc']
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

        

        self.fields['tipocontrato'].widget.attrs['style'] = "width:750px"
        self.fields['datecontrato'].widget.attrs['style'] = "width:120px"
        self.fields['parte2'].widget.attrs['style'] = "width:350px"
        self.fields['datecontrato_ini'].widget.attrs['style'] = "width:120px"
        self.fields['datecontrato_fin'].widget.attrs['style'] = "width:120px"
        self.fields['importeContrato'].widget.attrs['style'] = "width:160px"
        self.fields['status'].widget.attrs['readonly'] = True
        self.fields['imppContrato'].widget.attrs['style'] = "width:160px"
        self.fields['testigoContrato1'].widget.attrs['style'] = "width:350px"
        self.fields['testigoContrato2'].widget.attrs['style'] = "width:350px"

class PuestosForm(forms.ModelForm):
    class Meta:
        model=Puestos
        fields=['nombrePuesto', 'claveCampus', 'caracteristicasPuesto','conocimientosPuesto','experienciaPuesto','funcionesPuesto', 'habilidadesPuesto','herramientasPuesto']
        exclude = ['um','fm','uc','fc']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

        self.fields['nombrePuesto'].widget.attrs['style'] = "width:700px"
        self.fields['nombrePuesto'].widget.attrs['readonly'] = True
        self.fields['claveCampus'].widget.attrs['style'] = "width:700px"
        self.fields['claveCampus'].widget.attrs['readonly'] = True
        self.fields['caracteristicasPuesto'].widget.attrs['style'] = "width:700px"
        self.fields['conocimientosPuesto'].widget.attrs['style'] = "width:700px"
        self.fields['experienciaPuesto'].widget.attrs['style'] = "width:700px"
        self.fields['funcionesPuesto'].widget.attrs['style'] = "width:700px"
        self.fields['habilidadesPuesto'].widget.attrs['style'] = "width:700px"
        self.fields['herramientasPuesto'].widget.attrs['style'] = "width:700px"