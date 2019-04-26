from django.contrib.auth.models import AbstractUser
from django.db import models
from core.models import Core
from users.models import CustomUser
from taggit.managers import TaggableManager


class Company(Core):
    name = models.CharField(verbose_name="Company name", max_length=500,
                            null=True, blank=False)
    registered_name = models.CharField(verbose_name="Registered Company name", max_length=500,
                                       null=True, blank=True)
    no_employees = models.IntegerField(verbose_name="No of Employees",
                                       null=True, blank=True)
    website = models.URLField(
        verbose_name="Website", null=True, blank=True)
    hash_tags = TaggableManager()
    # More info at: https://www.revsys.com/tidbits/tips-using-djangos-manytomanyfield/
    #contacts = models.ManyToManyField('Contact', related_name='companies')

    class Meta:
        ordering = ('-created_on', 'name')
        #verbose_name_plural = "Company"

    def __str__(self):
        return self.name or ''


class Contact(Core):
    name = models.CharField(verbose_name="Full name", max_length=500,
                            null=True, blank=False)
    email = models.EmailField(verbose_name="Primary Email",
                              null=True, blank=False)
    primary_phone_no = models.CharField('Phone No', max_length=128,
                                        null=True, blank=False, default="")
    alt_phone_no = models.CharField('Alternate Phone No', max_length=128,
                                    null=True, blank=True, default="")
    address = models.TextField(verbose_name="Address",
                               null=True, blank=True)
    hash_tags = TaggableManager()
    parent_company = models.ForeignKey(
        'companies.company', related_name='members', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created_on', 'name')
        #verbose_name_plural = "Company"

    def __str__(self):
        return self.name or ''
