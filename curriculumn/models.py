from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class Standard(models.Model):
    name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(null=True,blank=True)
    description=models.TextField(max_length=500,blank=True)

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super().save(*args,**kwargs)

class Subject(models.Model):
    subject_id=models.CharField(max_length=100,unique=True)
    name=models.CharField(max_length=100)
    slug=models.SlugField(null=True,blank=True)
    standard=models.ForeignKey(Standard,on_delete=models.CASCADE,related_name='subjects')
    image=models.ImageField(upload_to='curriculumn/images',blank=True)
    description=models.TextField(max_length=500,blank=True)

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug=slugify(self.subject_id)
        super().save(*args,**kwargs)

class Lesson(models.Model):
    lesson_id=models.CharField(max_length=100,unique=True)
    standard=models.ForeignKey(Standard,on_delete=models.CASCADE)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE,related_name='lessons')
    name=models.CharField(max_length=250)
    position=models.PositiveBigIntegerField(verbose_name="chapter no.")
    slug=models.SlugField(null=True,blank=True)
    video=models.FileField(upload_to='curriculumn/videos',blank=True,null=True)
    ppt=models.FileField(upload_to='curriculumn/ppt',blank=True)
    notes=models.FileField(upload_to='curriculumn/notes',blank=True)

    class Meta:
        ordering = ['position']
    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super().save(*args,**kwargs)