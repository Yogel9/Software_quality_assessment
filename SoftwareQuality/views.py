import os

from fpdf import FPDF
from django.http import HttpResponse, FileResponse
from django.shortcuts import render


def main_index(request):
    """ Главная страница """
    context = {"title": 'Главная'}
    return render(request, 'base.html', {'context': context, })


def get_pdf(request):
    """ Отчёт в pdf """
    print(os.getcwd() + '\\DejaVuSansCondensed.ttf')
    data = request.POST.dict()
    del data['csrfmiddlewaretoken']

    spacing = 1
    pdf = FPDF()
    pdf.add_page()

    pdf.add_font('DejaVu', '', os.getcwd() + '\\DejaVuSansCondensed.ttf', uni=True)
    pdf.set_font('DejaVu', '', 14)

    col_width = pdf.w / 2
    row_height = pdf.font_size
    print(col_width)
    print(row_height)
    for row in data.items():
        for item in row:
            pdf.cell(col_width, row_height * spacing,
                     txt=item, border=1)
        pdf.ln(row_height * spacing)

    pdf.output('simple_table.pdf')
    return FileResponse(open('simple_table.pdf', 'rb'))

