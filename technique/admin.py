from django.contrib import admin
from django.forms import TextInput, Textarea
from embed_video.admin import AdminVideoMixin
from django.db import models
from .models import Technique


class TechniqueAdmin(AdminVideoMixin, admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':12, 'cols':60})},
    }
    pass
admin.site.register(Technique, TechniqueAdmin)


