from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    cost = models.IntegerField()
    created_date = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.title