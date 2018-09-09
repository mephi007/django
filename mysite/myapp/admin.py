from django.contrib import admin

# Register your models here.

from myapp.models import post

class PostModelAdmin(admin.ModelAdmin):
	list_display = ['title', 'updated', 'timestamp']
	list_display_links = ["updated"]
	list_filter = ["updated", "timestamp"]
	search_fields = ["title"]
	class Meta:
		model = post


admin.site.register(post, PostModelAdmin)
