from django.contrib import admin

from .models import Tag, TaggedItem
from .forms import TagAdminForm


class TagAdmin(admin.ModelAdmin):
    form = TagAdminForm


admin.site.register(TaggedItem)
admin.site.register(Tag, TagAdmin)
