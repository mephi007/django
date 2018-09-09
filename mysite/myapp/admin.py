from django.contrib import admin

# Register your models here.

from myapp.models import post

class PostModelAdmin(admin.ModelAdmin):
	list_display = ('title', 'updated', 'timestamp')
	class Meta:
		model = post


admin.site.register(post, PostModelAdmin)
