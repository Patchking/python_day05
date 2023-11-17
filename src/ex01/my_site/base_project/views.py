from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UploadFileForm
from .somewhere_else import handle_uploaded_file, get_mediafile_list
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return HttpResponse("<h1>Главная</h1>")

def about(request):
    return HttpResponse("<h1>Наш клуб</h1>")

@csrf_exempt
def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            is_audio = handle_uploaded_file(request.FILES["file"])
            if is_audio:
                return HttpResponse("Uploaded")
            else:
                return HttpResponse("Upload failed")
        else:
            print("form not valid")
            print(form.errors)
    else:
        form = UploadFileForm()
    return HttpResponse("Upload failed")

def get_list(request):
    return HttpResponse(str(get_mediafile_list()))

# Create your views here.
