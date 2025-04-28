from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    address = models.CharField(max_length=255)
    organization = models.ForeignKey('organizations.Organization', on_delete=models.CASCADE, related_name='events', null=True, blank=True)
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, related_name='events', null=True, blank=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-start_time']
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
        indexes = [
            models.Index(fields=['start_time']),
            models.Index(fields=['end_time']),
        ]
        constraints = [
            models.CheckConstraint(
                check=models.Q(start_time__lt=models.F('end_time')),
                name='start_time_before_end_time'
            ),
            models.CheckConstraint(
                check=models.Q(organization__isnull=False) | models.Q(user__isnull=False),
                name='either_organization_or_user'
            ),
        ]
