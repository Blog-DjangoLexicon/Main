from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS = (
    (0, 'Draft'),
    (1, 'Published')
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, defualt=0)

    def __str__(self):
        return self.title