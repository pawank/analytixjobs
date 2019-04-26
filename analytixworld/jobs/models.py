from django.contrib.auth.models import AbstractUser, User
from django.db import models
from core.models import Core
from users.models import CustomUser
from companies.models import Company
from phonenumber_field.modelfields import PhoneNumberField
from djmoney.models.fields import MoneyField


class Employer(models.Model):
    name = models.CharField(verbose_name="Company name", max_length=500,
                            null=True, blank=False)
    email = models.EmailField(verbose_name="Email", max_length=500,
                              null=True, blank=False)
    no_employees = models.IntegerField(verbose_name="No of Employees",
                                       null=True, blank=True)
    website = models.URLField(
        verbose_name="Website", null=True, blank=True)

    description = models.TextField(verbose_name="Description",
                                   null=True, blank=True)

    address = models.TextField(verbose_name="Description",
                               null=True, blank=False)
    '''
    primary_phone_no = PhoneNumberField(
        null=True, blank=True, default='+919000000000')
    alt_phone_no = PhoneNumberField(
        null=True, blank=True, default='+919000000000')
    fax_number = PhoneNumberField(
        null=True, blank=True, default='+919000000000')
    '''
    primary_phone_no = models.CharField('Phone No', max_length=128,
                                        null=True, blank=False, default="")
    alt_phone_no = models.CharField('Alternate Phone No', max_length=128,
                                    null=True, blank=True, default="")

    class Meta:
        ordering = ('name', )
        #verbose_name_plural = "Company"

    def __str__(self):
        return self.name


class Job(Core):
    source = models.CharField(verbose_name="Job Source",
                              max_length=255, null=True, blank=False)
    GENDERS = [('any', 'Any'), ('male', 'Male'),
               ('female', 'Female'), ('other', 'Other')]
    gender = models.CharField(verbose_name="Gender", choices=GENDERS,
                              max_length=255, null=True, blank=True, default='any')
    title = models.CharField(verbose_name="Job Title",
                             max_length=255, null=True, blank=False)
    info_url = models.URLField(
        verbose_name="Job Information URL", null=True, blank=True)
    employer = models.ForeignKey(
        'companies.company', related_name='employers', on_delete=models.CASCADE)
    JOB_TYPES = [('full-time', 'Full time'), ('freelance', 'Freelance'),
                 ('internship', 'Internship'), ('part-time', 'Part time'), ('contract', 'Contract')]
    job_type = models.CharField(verbose_name="Job Type",
                                max_length=255, null=True, blank=False, choices=JOB_TYPES, default='full-time')
    description = models.TextField(verbose_name="Job Description",
                                   null=True, blank=False)
    skills = models.TextField(verbose_name="Job Skills",
                              null=True, blank=True)
    education = models.TextField(verbose_name="Education",
                                 null=True, blank=True)
    experience = models.TextField(verbose_name="Experience",
                                  null=True, blank=True)
    location = models.CharField(verbose_name="Location",
                                max_length=500, null=True, blank=False)
    industry = models.CharField(verbose_name="Industry",
                                max_length=500, null=True, blank=False)
    starting_salary = MoneyField(max_digits=19, decimal_places=4,
                                 default_currency='USD', null=True, blank=True)
    ending_salary = MoneyField(max_digits=19, decimal_places=4,
                               default_currency='USD', null=True, blank=True)

    class Meta:
        ordering = ('-created_on', 'title',)
        #verbose_name_plural = "Job"
        pass

    def __str__(self):
        return self.title
