from django.db import models

from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone





class Home(models.Model):
    greeting = models.CharField(
        max_length=30, blank=True, null=True, verbose_name="Greetings (eg: Hello)")
    name = models.CharField(max_length=100, blank=True,
                            null=True, verbose_name="Full Name")
    image = models.ImageField(upload_to='myinfo')
    hiringskill = models.CharField(max_length=100, blank=True, null=True)
    par_inro = models.TextField(
        blank=True, null=True, verbose_name="Introduction")
    avatar_img = models.CharField(max_length=100, blank=True, null=True,
                                  verbose_name="Google Drive Image Id")
    hireMe_link = models.CharField(max_length=200, blank=True, null=True)
    cv_link = models.URLField(blank=True, null=True)

    

    def __str__(self):
        return self.name

class WorkExperience(models.Model):
    position = models.CharField(max_length=100)
    description = models.TextField()
    certificates = models.ImageField(upload_to='certificates')

    def __str__(self):
        return self.position

class MyInfo(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='myinfo')
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    date_of_birth = models.DateField(default='1970-01-01')
    current_date = models.DateField(auto_now=True)
    c_bro=models.IntegerField(default=0)
    c_sis=models.IntegerField(default=0)
    mother = models.CharField(max_length=100)
    father = models.CharField(max_length=100)
    brother = models.CharField(max_length=100)
    sister = models.CharField(max_length=100)
    des = models.TextField(
        blank=True, null=True, verbose_name="Introduction")
    def __str__(self):
        return self.name

class ExamCracked(models.Model):
    exam_type = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.exam_type

class ParticipationCertificate(models.Model):
    image = models.ImageField(upload_to='participation_certificates')

    def __str__(self):
        return self.image.name

class OtherSkill(models.Model):
    skill = models.CharField(max_length=100)

    def __str__(self):
        return self.skill


class Projects(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    skill = models.TextField(max_length=230, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='myinfo')

    def __str__(self):
        return self.title


class Contact(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)

    email = models.EmailField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    msg = models.TextField(max_length=100, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='myinfo')

    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)

    instagram = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class Skills(models.Model):
    top_skill = models.CharField(max_length=50, blank=True, null=True)
    level = models.CharField(max_length=50, blank=True, null=True)
    experience_dur = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.top_skill
    
class SocialMediaLinks(models.Model):
    name = models.CharField(max_length=80, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    social_icon = models.CharField(
        max_length=60, blank=True, null=True, verbose_name="Icon (eg: fa -fa-twitter)")

    
    def __str__(self):
        return self.social_icon
class GalleryImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='myinfo')

    def __str__(self):
        return self.title