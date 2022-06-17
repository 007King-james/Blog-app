from django.contrib import admin

# Register your models here.
from.models import text,author,created_date,published_date,Title

admin.site.register(text)
admin.site.register(author)
admin.site.register(created_date)
admin.site.register(published_date)
admin.site.register(Title)

