from django.db import models

# Create your models here.

class Author(models.Model):
    AuthorID = models.IntegerField()
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    gender = models.CharField(max_length=45)
    DOB = models.DateField()
    ContactID = models.CharField(max_length=45)

    def __str__(self):
        return self.AuthorID
    
class Book(models.Model):
    ISBN = models.IntegerField()
    title = models.CharField(max_length=45)
    publish_date = models.DateField()
    price = models.DecimalField(max_digits=3,decimal_places=2)

    def __str__(self):
        return self.ISBN

class Category(models.Model):
    CategoryCode = models.IntegerField(primary_key=True)
    CategoryDescription = models.CharField(max_length=45)

    def __str__(self):
        return self.CategoryCode