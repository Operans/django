from django.db import models

# Create your models here.
class Book(models.Model):
    GENRE = (
        ('Жанр', 'Жанр'),
        ('Боевик', 'Боевик'),
        ('Романтика', 'Романтика'),
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    genre = models.CharField(max_length=100, choices= GENRE, default = GENRE[0],  null=True)
    video = models.URLField(null=True)
    cost = models.IntegerField()
    created_date = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.title