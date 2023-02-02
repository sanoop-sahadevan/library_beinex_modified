from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()


    def __str__(self):
        return self.name


class Book(models.Model):
    title=models.CharField(max_length=100)
    
    summary=models.TextField()
    published_date=models.DateTimeField(auto_now_add=True)
    
    author=models.ForeignKey(Author,
    on_delete=models.SET_NULL,
    null=True

    )
