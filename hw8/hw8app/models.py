from django.db import models

# Create your models here.
class Post(models.Model) :
    category = models.CharField(max_length=10)
    title = models.CharField(max_length=10)
    content = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title