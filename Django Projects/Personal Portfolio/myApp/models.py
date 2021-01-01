from django.db import models


# Create your models here.
class PersonalBlog(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    upload = models.ImageField(default='default.jpg', upload_to='blog_pics/')
    description = models.TextField(null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
