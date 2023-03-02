from django.contrib import admin
from . models import Post

class Postadmin(admin.ModelAdmin):
    list_display=('pk','text','pub_date','author')
    list_filter=('pub_date')
    search_fields=('text')
admin.site.register(Post)
