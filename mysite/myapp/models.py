from django.db import models
from django.urls import reverse

# Create your models.Models here.

class post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title

    def get_absolut_url(self):
    	return reverse("detail", kwargs={"id": self.id})
    	# return "/%s"%(self.id)

