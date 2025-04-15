from django.db import models
from django.contrib.auth.models import User  

# Create your models here
class Author(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    year_of_birth=models.IntegerField()
    county=models.CharField(max_length=50,null=True,blank=True)
    biography=models.TextField(null=True,blank=True)
    def __str__(self):
        return self.first_name+" "+self.last_name


class Publication(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    address_1=models.CharField(max_length=50)
    house_number=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    def __str__(self):
        return self.name+" "+self.address

class Book(models.Model):
    title=models.CharField(max_length=50)
    isbn=models.CharField(max_length=17)
    short_content=models.TextField(null=True,blank=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    cover_page=models.ImageField(upload_to="book_covers/",blank=True,null=True)
    author=models.ForeignKey(Author, on_delete=models.CASCADE)
    publication=models.ForeignKey(Publication, on_delete=models.CASCADE)


class PublicationsAuthor(models.Model):
    author=models.ForeignKey(Author, on_delete=models.CASCADE)
    publication=models.ForeignKey(Publication, on_delete=models.CASCADE)





