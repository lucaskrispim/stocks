from django import forms

class StockRangeForm(forms.Form):
    nome = forms.CharField(label="Sigla Ação",max_length=100)
    data_inicial = forms.DateField(input_formats=['%Y-%m-%d'], widget=forms.DateInput(attrs={'type': 'date'}))
    data_final = forms.DateField(input_formats=['%Y-%m-%d'], widget=forms.DateInput(attrs={'type': 'date'}))