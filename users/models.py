from django.db import models

from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    # For random images from picsum.photos, we'll store the ID
    random_image_id = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    view_count = models.IntegerField(default=0)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
    
    def save(self, *args, **kwargs):
        # If no image is uploaded and no random image ID is set, generate one
        if not self.image and not self.random_image_id:
            import random
            self.random_image_id = random.randint(1, 1000)
        super().save(*args, **kwargs)
