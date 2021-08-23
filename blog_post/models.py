from django.db import models
from user_account.models import Account
from PIL import Image

# Create your models here.

class Category(models.Model):
  name = models.CharField(max_length=20)
  
  def __str__(self):
    return self.name

class Post(models.Model):
  title = models.CharField(max_length=255)
  created_by = models.ForeignKey(Account, on_delete=models.CASCADE)
  body  = models.TextField()
  created = models.DateTimeField(auto_now_add=True)
  last_modified = models.DateTimeField(auto_now=True)
  image         = models.ImageField(default='post_pics/default.jpg',upload_to='post_pics',null=True,blank=True)
  categories = models.ManyToManyField('Category',related_name='posts')
  
  
  def __str__(self):
    return self.title
  
  def save(self,*args, **kwargs):
    super().save()
    img = Image.open(self.image.path)
    
    if img.height > 300 or img.width > 300:
       output_size = (300,300)
       img.thumbnail(output_size)
       img.save(self.image.path)


class Comment(models.Model):
  author = models.ForeignKey(Account, on_delete=models.CASCADE)
  body   = models.TextField()
  reply  = models.ForeignKey('self',null=True,related_name="replies",on_delete=models.CASCADE)
  created = models.DateTimeField(auto_now_add=True)
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.author.username
  
 