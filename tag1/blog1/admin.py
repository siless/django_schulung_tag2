from django.contrib import admin

# Register your models here.
from .models import Post, AbstractModel


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    #list_display = ['deleted', 'title', 'content']
    fieldsets = ('Test_fieldsets', {
            'fields': (('title', 'deleted'), 'content')
        }),
    list_per_page = 1
    pass
