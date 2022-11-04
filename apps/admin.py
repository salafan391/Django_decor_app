from django.contrib import admin
from .models import About, Offer, Project
# Register your models here.

admin.site.register(Offer)
admin.site.register(Project)
admin.site.register(About)

