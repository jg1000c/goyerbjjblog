from django.contrib import admin

from embed_video.admin import AdminVideoMixin

from .models import Lucas


class PostAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass


admin.site.register(Lucas, PostAdmin)