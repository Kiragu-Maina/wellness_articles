from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200, null=True, blank=True)
    author = models.CharField(max_length=200, null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    short_description = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    published_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    readmoreurl = models.URLField(null=True, blank=True)
    
    def save(self, *args, **kwargs):
        # Truncate the title and author fields if they exceed their maximum length
        if len(self.title) > self._meta.get_field('title').max_length:
            self.title = self.title[:self._meta.get_field('title').max_length]
        if len(self.author) > self._meta.get_field('author').max_length:
            self.author = self.author[:self._meta.get_field('author').max_length]

        # Call the original save method to save the instance
        super().save(*args, **kwargs)


    # Add more relevant fields as needed

    def __str__(self):
        return self.title
