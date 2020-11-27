from django.db import models

# Create your models here.
class Book(models.Model):
    Book_name=models.CharField(max_length=120)
    author=models.CharField(max_length=120)
    pages=models.IntegerField(default=100)
    price=models.IntegerField(default=100)

    def __str__(self):
        return self.Book_name