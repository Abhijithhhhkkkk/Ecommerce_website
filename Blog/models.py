from io import BytesIO
from django.db import models
from django.core.files.base import ContentFile
from django.contrib.auth.models import User
from PIL import Image


def resize_image_field(field, max_height=700):
    """
    Resize an ImageField in-place, works with any storage backend
    (S3, local, etc.) since it never touches `.path`.
    Returns True if the field was modified.
    """
    if not field:
        return False
    field.open()
    image = Image.open(field)
    image.load()  # force read before file handle closes
    if image.height <= max_height:
        return False

    new_width = int((max_height / image.height) * image.width)
    image = image.resize((new_width, max_height))

    buffer = BytesIO()
    image_format = (image.format or 'JPEG')
    if image_format == 'JPEG' and image.mode in ('RGBA', 'P'):
        image = image.convert('RGB')
    image.save(buffer, format=image_format, quality=95, optimize=True)
    buffer.seek(0)

    field.save(field.name, ContentFile(buffer.read()), save=False)
    return True


class Homepage(models.Model):
    title = models.CharField(max_length=100)
    img_1 = models.ImageField(upload_to='hero_banner/', blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if resize_image_field(self.img_1):
            super().save(update_fields=['img_1'])


class logo(models.Model):
    title = models.CharField(max_length=100)
    img_2 = models.ImageField(upload_to='logo/', blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if resize_image_field(self.img_2, max_height=200):
            super().save(update_fields=['img_2'])


class details(models.Model):
    Category = [
        ('shirt', 'Shirt'),
        ('pant', 'Pant'),
        ('shoes', 'Shoes'),
        ('linen Co-ord Set', 'Linen Co-ord Set'),
        ('Modern Kurta', 'Modern kurta'),
        ('slip Dress', 'Slip Dress'),
    ]
    title = models.CharField(max_length=100)
    decription = models.TextField()
    price = models.IntegerField()
    category = models.CharField(max_length=100, choices=Category)
    img_3 = models.ImageField(upload_to='details/', blank=True, null=True)
    img_4 = models.ImageField(upload_to='details/', blank=True, null=True)
    img_5 = models.ImageField(upload_to='details/', blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        resized = []
        for field_name in ['img_3', 'img_4', 'img_5']:
            field = getattr(self, field_name)
            if resize_image_field(field):
                resized.append(field_name)
        if resized:
            super().save(update_fields=resized)


class order_details(models.Model):
    product = models.ForeignKey(details, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order: {self.product.title} placed by {self.buyer.email}"