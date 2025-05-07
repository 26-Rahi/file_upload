from django import forms
from .models import UploadedFile
import os


ALLOWED_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.pdf', '.docx']
MAX_FILE_SIZE = 2 * 1024 * 1024  # 2MB

class UploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file']

    def clean_file(self):
        file = self.cleaned_data.get('file')

        # Validate extension
        ext = os.path.splitext(file.name)[1].lower()
        if ext not in ALLOWED_EXTENSIONS:
            raise forms.ValidationError(f"Not allowed file type: {ext}")

        # Validate size
        if file.size > MAX_FILE_SIZE:
            raise forms.ValidationError("File size must be under 2MB")

        return file