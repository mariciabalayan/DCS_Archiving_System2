from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Django Admin. Register models below
from django.contrib import admin

# Create your models here.
class College(models.Model):
    name            = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name

class Department(models.Model):
    name            = models.CharField(max_length=64)
    college         = models.ForeignKey(College)

    def __unicode__(self):
        return self.name + ", " + self.college.name

class Course(models.Model):
    name            = models.CharField(max_length=64)
    department      = models.ForeignKey(Department)

    def __unicode__(self):
        return self.name + ", " + self.department.name


#class UserProfile(models.Model):
#    user            = models.OneToOneField(User)
#    middlename      = models.CharField(max_length=32, null=True, blank=True)
#    photo           = models.FileField(upload_to='photos', null=True, blank=True)
#    birthday        = models.DateField(null=True, blank=True)
#    course          = models.ForeignKey(Course, null=True, blank=True)
#    highest_degree_attained = models.CharField(max_length=100, null=True, blank=True)
#    length_of_service       = models.CharField(max_length=100, null=True, blank=True)

#    def save(self, *args, **kwargs):
#        if not self.pk:
#            try:
#                p = UserProfile.objects.get(user=self.user)
#                self.pk = p.pk
#            except UserProfile.DoesNotExist:
#                pass
#        super(UserProfile, self).save(*args, **kwargs)

#    def __unicode__(self):
#        return self.user.username+': '+ self.user.last_name + ", " + self.user.first_name

class Faculty(models.Model):
    user            = models.ForeignKey(User)
    first_name      = models.CharField(max_length=64)
    middle_name     = models.CharField(max_length=32, null=True, blank=True)
    last_name       = models.CharField(max_length=32)
    photo           = models.FileField(upload_to='photos', null=True, blank=True)
    birthday        = models.DateField(null=True, blank=True)
    course          = models.ForeignKey(Course, null=True, blank=True)
    highest_degree_attained = models.CharField(max_length=100, null=True, blank=True)
    length_of_service       = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.last_name+", "+ self.first_name

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = Faculty.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)

class Alternate_email(models.Model):
    user            = models.ForeignKey(User)
    email_address   = models.CharField(max_length=100)

    def __unicode__(self):
        return self.email_address 


class Contact(models.Model):
    user             = models.ForeignKey(User)
    contact_number   = models.CharField(max_length=20)

    def __unicode__(self):
        return self.contact_number 

class Address(models.Model):
    user            = models.ForeignKey(User)
    address         = models.CharField(max_length=100)

    def __unicode__(self):
        return self.address 
    
class Transaction(models.Model):
    name            = models.CharField(max_length=100)
    

    def __unicode__(self):
        return self.name
        
class File(models.Model):
    filename        = models.CharField(max_length=100)
    file            = models.FileField(upload_to='files/%Y')
    delete			= models.BooleanField(default=0)

    def __unicode__(self):
        return self.filename

class Dokument(models.Model):
    faculty         = models.ForeignKey(Faculty)
    transaction     = models.ForeignKey(Transaction)
    files           = models.ManyToManyField(File)
    
    def __unicode__(self):
        return self.faculty.last_name+", "+ self.faculty.first_name+ ": "+ self.transaction.name

class Log(models.Model):

    user            = models.ForeignKey(User)
    action          = models.CharField(max_length=100)
    file            = models.ForeignKey(File, null=True, blank=True)
    timestamp       = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return str(self.user) + " " + self.action + " " + str(self.file) + " " + str(self.timestamp)
        
    @classmethod
    def create(cls, user, action, file):
        log = cls(user=user, action=action, file=file)
        return log

# Register Models to Django Admin
admin.site.register(Dokument)
admin.site.register(Department)
admin.site.register(College)
admin.site.register(Course)
admin.site.register(Alternate_email)
admin.site.register(Contact)
admin.site.register(Address)
admin.site.register(Transaction)
admin.site.register(Faculty)
admin.site.register(File)
admin.site.register(Log)
