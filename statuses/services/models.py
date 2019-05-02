from django.db import models
from django.utils.text import slugify


class ServiceGroup(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, allow_unicode=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name, allow_unicode=True)
        super().save(force_insert, force_update, using, update_fields)


class ServiceStatus(models.Model):
    name = models.CharField(max_length=30, unique=True)
    short_description = models.CharField(max_length=100)
    description = models.TextField()
    is_ok = models.BooleanField(default=False)
    enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Service(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, allow_unicode=True)
    groups = models.ManyToManyField(ServiceGroup, related_name='groups')
    status = models.PositiveIntegerField(default=0)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name, allow_unicode=True)
        super().save(force_insert, force_update, using, update_fields)
