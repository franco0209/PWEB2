from django.shortcuts import render
from django.http import Http404
import datetime
from model_example import renderers

def pdf_view(request, *args, **kwargs):
    data = {
        'today': datetime.date.today(), 
        'amount': 39.99,
        'customer_name': 'Cooper Mann',
        'invoice_number': 1233434,
    }
    print(data)
    return renderers.render_to_pdf('pdfs/invoice.html', data)
