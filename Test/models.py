from django.db import models


class Question(models.Model):
    question = models.CharField(max_length=300)

    def __str__(self):
        return "问题" + self.id

    class Meta:
        ordering = ["id"]
        verbose_name = "问题"
        verbose_name_plural = "问题"


