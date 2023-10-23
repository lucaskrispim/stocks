from django import forms

class StockRangeForm(forms.Form):
    nome = forms.CharField(label="Sigla Ação",max_length=100,required=True,error_messages={'required': 'Por favor, insira uma sigla de uma ação brasileira.'})
    data_inicial = forms.DateField(input_formats=['%Y-%m-%d'], widget=forms.DateInput(attrs={'type': 'date'}),error_messages={'required': 'Por favor, insira uma data válida.'})
    data_final = forms.DateField(input_formats=['%Y-%m-%d'], widget=forms.DateInput(attrs={'type': 'date'}),error_messages={'required': 'Por favor, insira uma data válida.'})