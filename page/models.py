from django.db import models

# Create your models here.

STATUS = [
    ('draft',  'Taslak'),
    ('published', 'Yayinlandi'),
    ('deleted', 'Silindi'),
]


class Page(models.Model):
    title = models.CharField(max_length=200)
    # slug = models.SlugField
    content = models.TextField()
    cover_image = models.ImageField(upload_to='page')
    status = models.CharField(
        default="draft",
        choices=STATUS,
        max_length=10,
    )
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
