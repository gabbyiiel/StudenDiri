from flask import Blueprint, render_template, request, flash, redirect

from . import printing
from .models import PrintingService

@printing.route('/printing/request', methods=['GET', 'POST'])
def req_print():
    title = "Print"
    if request.method == 'POST':
        file = request.form.get('file')
        no_copies = request.form.get('no_copies')
        specification = request.form.get('specification')
        upload = PrintingService.add_print_request(file,no_copies,specification)
        print(upload)


    return render_template("Printing/base.html", title=title)