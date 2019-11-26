from django.db import models
from common.models import IndexedTimeStampedModel
from django.utils.translation import ugettext_lazy as _
from users.models import User

class Laboratory(IndexedTimeStampedModel):
    name = models.CharField(max_length=200)
    typo = models.CharField(max_length=100)
    location = models.CharField(max_length=150)
    users = models.ManyToManyField(User)

    class Meta:
        verbose_name_plural = "laboratories"

    def __str__(self):
        return self.name