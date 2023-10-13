from django.shortcuts import render
from .forms import StockRangeForm
import yfinance as yf
import math

# Create your views here.
def index(request):

    if request.method == 'POST':

        form = StockRangeForm(request.POST)

        if form.is_valid():

            try:
                df2 = yf.download(f"{form.data['nome']}.sa",start=f"{form.data['data_inicial']}",end=f"{form.data['data_final']}", progress=False)
                print(df2)
            except Exception as e:
                print(f"Erro: {e}")

            context = {
            'form':StockRangeForm
            }

            return render(request, 'index.html',context=context)
    
    context = {
        'form':StockRangeForm
    }

    return render(request, 'index.html',context=context)