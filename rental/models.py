from django.db import models
from django.conf import settings



class OwnedModel(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    class Meta:
        abstract=True


class Belonging(OwnedModel):
    name=models.CharField(max_length=100)

# Create your models here.
class Friend(models.Model):
    name=models.CharField(max_length=100)
    
    def __repr__(self):
        return self.name


class Belonging(models.Model):
    name=models.CharField(max_length=100)

    def __repr__(self):
        return self.name


class Borrowed(models.Model):
    what=models.ForeignKey(Belonging,on_delete=models.CASCADE)
    to_who=models.ForeignKey(Friend,on_delete=models.CASCADE)
    when=models.DateTimeField(auto_now_add=True)
    returned=models.DateTimeField(auto_now=True)

    def __repr__(self):
        return self.when
