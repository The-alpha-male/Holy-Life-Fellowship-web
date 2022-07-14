from django.contrib import admin

from . models import Contactus,Gallery,Events

# # Register your models here.
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title','caption','created_date']
    list_filter = ['created_date']
    search_fields = ['title','caption']
    list_per_page = 10
    ordering = ['-created_date']
    prepopulated_fields = {'slug':('title',)}
    class Meta:
        model = Gallery
admin.site.register(Contactus)
admin.site.register(Gallery,GalleryAdmin)
admin.site.register(Events)

