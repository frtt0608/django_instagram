from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    content = models.TextField()
    hit = models.IntegerField(default=0)

    # image = models.ImageField()
    
    # thumbnail_fit = ProcessedImageField(
    #         blank = True,
    #         upload_to = board_image_path,
    #         processors = [ResizeToFit(300, 300)],
    #         format = 'JPEG',
    #         options = {'quality':90},
    #     )
    
    def __str__(self):
        return f'POST : {self.pk}'
    
    def get_absolute_url(self):
        return reverse('posts:posts_detail', args=[self.pk])
    
class Image(models.Model):
    file = models.ImageField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    