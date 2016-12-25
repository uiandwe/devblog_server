from django.contrib import admin

from .models import Blog

class BlogModelAdmin(admin.ModelAdmin):
   list_display = ["title", "created_at"]
   list_display_links = ["created_at"]
   list_editable = ["title"]

   search_fields = ["title", "content"]
   class Meta:
      model = Blog


admin.site.register(Blog, BlogModelAdmin)
