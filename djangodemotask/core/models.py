from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Create your models here.


class Question(models.Model):
    """ Question models """
    title = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, related_name='question', on_delete=models.CASCADE)
    tags = TaggableManager()

    class Meta:
        ordering = ("-created_at", )

    def __str__(self):
        if len(self.title) > 15:
            return f"{self.id}: {self.title[:15]}..."
        else:
            return f"{self.id}: {self.title}"

    def ___unicode__(self):
        if len(self.title) > 15:
            return f"{self.id}: {self.title[:15]}..."
        else:
            return f"{self.id}: {self.title}"

    # def get_absolute_url(self):
    #     pass
