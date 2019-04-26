from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models


class CustomUser(AbstractUser):
    avatar_url = models.URLField(
        verbose_name="Avatar URL", null=True, blank=True)
    address = models.TextField(verbose_name="Address",
                               null=True, blank=True)
    permanent_address = models.TextField(verbose_name="Permanent Address",
                                         null=True, blank=True)
    '''
    primary_phone_no = PhoneNumberField('Phone No',
                                        null=True, blank=True, default="")
    alt_phone_no = PhoneNumberField('Alternate Phone No',
                                    null=True, blank=True, default="")
    '''
    primary_phone_no = models.CharField('Phone No', max_length=128,
                                        null=True, blank=False)
    alt_phone_no = models.CharField('Alternate Phone No', max_length=128,
                                    null=True, blank=True, default="")

    def __str__(self):
        return self.email or ''
