from django.db import models


class Profession(models.Model):
    type1 = models.CharField(max_length=128)
    type2 = models.CharField(max_length=128)
    profession_name = models.CharField(max_length=256)

    def __str__(self):
        return self.profession_name

    class Meta:
        ordering = ["id"]
        verbose_name = "专业信息"
        verbose_name_plural = "专业信息"
