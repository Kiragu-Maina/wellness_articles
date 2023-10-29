from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    author = models.CharField(max_length=200, null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    short_description = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    published_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    readmoreurl = models.URLField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # Truncate values that exceed the maximum length
        max_length = 200

        if self.title:
            self.title = self.title[:max_length]

        if self.category:
            self.category = self.category[:max_length]

        if self.author:
            self.author = self.author[:max_length]

        super().save(*args, **kwargs)
    def __str__(self):
        return self.title

