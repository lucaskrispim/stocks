from django.shortcuts import render
from .forms import StockRangeForm
import yfinance as yf
from .indicators import RSI
import math
from django.http import HttpResponse
from datetime import datetime, timedelta
import numpy as np

# Create your views here.
def index(request):

    if request.method == 'POST':

        form = StockRangeForm(request.POST)

        if form.is_valid():

            try:
                date_obj = datetime.strptime(form.data['data_inicial'], '%Y-%m-%d')

                result_date = date_obj - timedelta(days=100)

                df2 = yf.download(f"{form.data['nome']}.sa",start=f"{result_date.strftime('%Y-%m-%d')}",end=f"{form.data['data_final']}", progress=False)
                
                data = []
                data = RSI(data=df2,column='Close', window=14)

                vol = round(data['Variation'].std(),2)

                avg_return = round(data['Variation'].mean(),2)

                var = round(np.quantile(data['Variation'][:], 0.05),2)
                data = data.round(2)
                data.reset_index(level=0, inplace=True)
                data = data[data['Date'] >= form.data['data_inicial']]
                data['Date'] = data['Date'].dt.strftime('%d-%m-%Y')
                data = data.to_dict(orient='records')

                context = {
                    'sigla':form.data['nome'],
                    'form':StockRangeForm,
                    'companies':data,
                    'vol':vol,
                    'avg_return':avg_return,
                    'var':var
                }

            except Exception as e:
                print(f"Erro: {e}")
                context = {
                    'companies':[],
                    'erro':'Ocorreu um erro na obtenção dos indicadores da empresa ou a sigla da empresa está incorreta!',
                    'form':StockRangeForm,
                }

            finally:
                return render(request, 'index.html',context=context)
    
    context = {
        'form':StockRangeForm
    }

    return render(request, 'index.html',context=context)