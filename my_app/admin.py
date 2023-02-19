from django.contrib import admin
from .models import Sunglasses, Brand, Color, Type

# to register the models in the admin page
admin.site.register(Sunglasses)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Type)