from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='content_pics')

    def save(self, **kwargs):
        super().save(**kwargs)

        image = Image.open(self.image.path)

        if image.height > 600 or image.width > 600:
            output_size = (600, 600)
            image.thumbnail(output_size)
            image.save(self.image.path)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
