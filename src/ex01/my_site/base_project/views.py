from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UploadFileForm
from .somewhere_else import handle_uploaded_file, get_mediafile_list, getfile
from django.views.decorators.csrf import csrf_exempt

def redirect_list(request):
    return HttpResponseRedirect("/list/")

@csrf_exempt
def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            is_audio = handle_uploaded_file(request.FILES["file"])
            if is_audio:
                return HttpResponse("Uploaded")
            else:
                return HttpResponse("Non-audio file detected")
        else:
            print("form not valid")
            print(form.errors)
    else:
        form = UploadFileForm()
    return render(request, "upload.html", {"form": form, "data": get_mediafile_list()})

def get_list(request):
    return HttpResponse(str(get_mediafile_list()))

def get_file(request, filename):
    filetext = getfile(filename)
    response = HttpResponse(filetext, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response


# Create your views here.
