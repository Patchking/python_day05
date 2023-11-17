
from pathlib import Path
from django.conf import settings
import mimetypes
import os

def handle_uploaded_file(file) -> bool:
    type = mimetypes.guess_type(file.name)[0]
    if not type:
        return False
    type = type.split("/")[0]
    if type != "audio":
        return False
    with open(settings.MEDIA_ROOT / file.name, "wb") as dest:
        for chunk in file.chunks():
            dest.write(chunk)
    return True

def get_mediafile_list():
    return os.listdir(settings.MEDIA_ROOT)

def getfile(filename):
    filename = settings.MEDIA_ROOT / filename
    if not os.path.exists(filename):
        return (False, None)
    with open(filename, "rb") as f:
        return (True, f.read())