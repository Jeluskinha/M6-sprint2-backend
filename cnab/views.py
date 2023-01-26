from django.http import HttpResponseRedirect
from django.shortcuts import render
# from .forms import UploadFileForm

with open("../CNAB.txt", "r") as source:
  data = source.read()  
  print(data)
  print('Tipo', data[0:1])
  print('Data', data[2:9])
  print('Valor', data[10:19])
  print('CPF', data[20:30])
  print('Cartão', data[31:42])
  print('Hora', data[43:48])
  print('Dono da loja', data[49:62])
  print('Nome da loja', data[63:81])


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            data(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def handle_uploaded_file(f):
    with open('CNAB.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    
    print(destination)