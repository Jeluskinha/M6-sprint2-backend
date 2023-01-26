from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm

with open("CNAB.txt", "r") as source:
  data = source.read()
  print(data)

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            data(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})