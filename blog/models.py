from django.db import models
from django.db.models.enums import Choices
from django.utils.timezone import now
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class BlogPost(models.Model):
    id = models.AutoField(primary_key=True)
    feature_image = models.ImageField()
    city = models.CharField(max_length=20, default="dehradun")
    country = models.CharField(max_length=20, default="India")
    title = models.CharField(max_length=100)
    description = RichTextUploadingField(blank=True, null=True)
    author_name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=20)
    time = models.DateTimeField(blank=True)
    post_view= models.IntegerField(default=0,null=True,blank=True)

    def __str__(self):
        return self.title


class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email =models.EmailField()
    comment = models.TextField()
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)


    def __str__(self):
        return str(self.sno)