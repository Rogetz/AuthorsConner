from django.contrib import admin

# Register your models here.
from myTestApp.models import MyBookModel,Book,Publisher,Author


# for any model created to be visible in the admin gui you must register it. so you first of all import the model.
admin.site.register(MyBookModel)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book)


