from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Link(models.Model):
    url = models.CharField(max_length=1000)
    date_posted = models.DateTimeField(default=timezone.now)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Link."""

        verbose_name = 'Link'
        verbose_name_plural = 'Links'

    def __str__(self):
        """Unicode representation of Link."""
        return self.url
