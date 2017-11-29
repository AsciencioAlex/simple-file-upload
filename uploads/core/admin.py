from django.contrib import admin

from uploads.core.forms import DocumentForm
from uploads.core.models import Document


admin.site.register(Document)
