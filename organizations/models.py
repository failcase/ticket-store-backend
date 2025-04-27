from django.db import models
from django_resized import ResizedImageField
from django.template.defaultfilters import slugify


class Organization(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(default="", null=False, blank=False, unique=True, db_index=True)
    description = models.TextField(blank=True, null=True)
    logo = ResizedImageField(size=[512, 512], crop=['middle', 'center'], force_format='JPEG', quality=90, blank=True, null=True)
    owner = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, related_name='organizations')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('organizations:organization_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
