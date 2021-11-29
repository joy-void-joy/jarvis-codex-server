from django.db import models
from django.utils import timezone
from django.conf import settings


class Log (models.Model):
    class Meta:
        verbose_name = "Log"
        verbose_name_plural = "Logs"
        ordering = ["pk"]

    sent_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.TimeField(default=timezone.now)
    command = models.CharField(max_length=200)
    answer = models.TextField()
    num_tokens = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    locked = models.BooleanField(default=False)

    def __str__(self):
        return f"# Command: {self.command}\n{self.answer}"

