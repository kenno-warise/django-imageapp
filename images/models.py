from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import Thumbnail


class Image(models.Model):
    image = models.ImageField(upload_to='img')
    image_medium = ImageSpecField(
            source='image',
            processors=[Thumbnail(700, 600)],
            format='JPEG',
            options={'quality':100}
    )
    image_small = ImageSpecField(
            source='image',
            processors=[Thumbnail(200, 100)],
            format='JPEG',
            options={'quality': 60}
    )
    created_at = models.DateField(auto_now_add=True)


