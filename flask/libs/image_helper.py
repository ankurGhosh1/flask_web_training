import os
import re

from werkzeug.datastructures import FileStorage
from flask_uploads import UploadSet, IMAGES

IMAGE_SET = UploadSet('images', IMAGES)

def save(image: FileStorage, folder, name):
    return IMAGE_SET.save(image, folder, name)


def path(filename, folder):
    return IMAGE_SET.path(filename, folder)
