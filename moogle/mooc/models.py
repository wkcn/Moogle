from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField()

    def is_authenticated():
        return True

    def __str__(self):
        return "User <%s>" % self.username