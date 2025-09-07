from django.contrib import admin
from .models import Post, Contact
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author','title','status','created_at')
    list_filter = ('status','created_at')
    search_fields = ('title','body')

    def image_preview(self,obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="100" height="100" />'
        return "Rasm yo'q"
    
    image_preview.allow_tags = True
    image_preview.short_description = 'Rasm oldindan ko\'rish'

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','created_at')
    search_fields = ('name','email','message')
    list_filter = ('created_at',)