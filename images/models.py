from django.db import models


class Image(models.Model):
    image = models.ImageField(
            upload_to='img/',
            height_field='url_height',
            width_field='url_width',
    )
    url_height = models.IntegerField(editable=False)
    url_width = models.IntegerField(editable=False)
    created_at = models.DateField(auto_now_add=True)


