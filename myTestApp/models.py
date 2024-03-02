#from django.contrib.auth.models import AbstractUser
from djongo import models
#from django.urls import reverse

class MyBookModel(models.Model):
    # help text is used in user forms to help them key in the right data.
    title = models.CharField(max_length=20,help_text='enter title of the book')
    author = models.CharField(max_length=20,help_text="author's name")

    #metadata
    #useful for customizing your model such as ordering, e.t.c
    class Meta:
        # the minus(-) sign before the title here is to reverse the sorting order, ordering here will be based on the title.
        ordering = ['-title']

    """def get_absolute_url(self):
        # returns the url to access a particular instance of my myBookModel
        return reverse('model-detail-view',args= [str(self.id)])"""

    def __str__(self):
        #This is a string to represent myBookModel object in adminSite e.t.c
        return self.title


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        #This is a string to represent myBookModel object in adminSite e.t.c
        return self.name

class Author(models.Model):
    salutation = models.CharField(max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    headshot = models.ImageField(upload_to='./tmp')

    def __str__(self):
        #This is a string to represent myBookModel object in adminSite e.t.c
        return self.first_name

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher,null=True,on_delete=models.CASCADE)
    publication_date = models.DateField()

    def name(self):
        return self.publisher.name

    def __str__(self):
        #This is a string to represent myBookModel object in adminSite e.t.c
        return self.title