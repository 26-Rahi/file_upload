from django.shortcuts import render, redirect
from .forms import UploadForm
from .models import UploadedFile


def upload_file(request):
    files = UploadedFile.objects.all()
    if request.method == 'POST':
        if files.count() >= 5:
            return render(request, 'upload.html', {
                'form': UploadForm(),
                'error': 'Maximum 5 files allowed.',
                'files': files
            })
        
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload')
    else:
        form = UploadForm()

    return render(request, 'upload.html', {'form': form, 'files': files})

# Create your views here.
