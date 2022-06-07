from django.db import models

# Create your models here.
DEFAULT_STATUS = "draft"
STATUS = [
    ('draft',  'Taslak'),
    ('published', 'Yayinlandi'),
    ('deleted', 'Silindi'),
]


class Page(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, null=True)
    content = models.TextField()
    cover_image = models.ImageField(upload_to='page',  null=True,  blank=True)
    status = models.CharField(
        default=DEFAULT_STATUS,
        choices=STATUS,
        max_length=10,
    )
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class Carousel(models.Model):
    title =  models.CharField(max_length=200,  blank=True, null=True)
    cover_image = models.ImageField(
        upload_to= "carousel",
        null=True,
        blank= True,
    )
    status =  models.CharField(
        default =  DEFAULT_STATUS,
        choices= STATUS,
        max_length=10,
    )
    create_at =  models.DateTimeField(auto_now_add=True)
    uptate_at =  models.DateTimeField(auto_now=  True)