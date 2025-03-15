from django.db import models

# Create your models here.
class Author(models.Model):
    '''
    An Author model for registering Book Authors.
    '''
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    '''
    This model is aiming for registering books.
    '''
    title = models.CharField(max_length=50)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title