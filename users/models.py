from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from common.models import IndexedTimeStampedModel

from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin, IndexedTimeStampedModel):
    email = models.EmailField(max_length=300, unique=True)
    name = models.CharField(max_length=200)
    is_staff = models.BooleanField(
        default=False,
        help_text=_('Designates whether this user can log into this admin site.'))
    is_active = models.BooleanField(
        default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    
    objects = UserManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return self.name

    def __str__(self):
        return self.email
