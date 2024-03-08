from django.db import models
from django.contrib.auth.models import User
# Create your models here.
"""
class Card(models.Model):
    id = models.UUIDField(primary_key = True, unique=True)
    name = models.CharField(max_length=100)
    set_id = models.UUIDField()
    set_name = models.CharField(max_length=50)
    img_url = models.URLField(max_length=200)


class LibraryCards(models.Model):
    library_owner = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    card_id = models.ForeignKey(Card.id)
"""