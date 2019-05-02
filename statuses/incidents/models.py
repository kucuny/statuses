from django.db import models
from django.utils.text import slugify

from statuses.services.models import Service, ServiceStatus


class IncidentStatus(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, allow_unicode=True)
    service_status = models.ForeignKey(ServiceStatus,
                                       related_name='incident_statuses', on_delete=models.NOT_PROVIDED)
    bg_color = models.CharField(max_length=10)
    text_color = models.CharField(max_length=10)
    enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name, allow_unicode=True)
        super().save(force_insert, force_update, using, update_fields)


class Incident(models.Model):
    service = models.ForeignKey(Service, related_name='incidents')
    title = models.CharField(max_length=200)
    incident_status = models.ForeignKey(IncidentStatus,
                                        related_name='incidents', on_delete=models.NOT_PROVIDED)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class IncidentHistory(models.Model):
    incident = models.ForeignKey(Incident,
                                 related_name='incident_histories', on_delete=models.CASCADE)
    incident_status = models.ForeignKey(IncidentStatus,
                                        related_name='incident_histories', on_delete=models.NOT_PROVIDED)
    message_type = models.CharField(max_length=10)
    messages = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)
        self.incident.incident_status = self.incident_status
