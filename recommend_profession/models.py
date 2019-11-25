from django.db import models


class Profession(models.Model):
    type1 = models.CharField(max_length=128)
    type2 = models.CharField(max_length=128)
    profession_name = models.CharField(max_length=256)
    profession_hot = models.CharField(max_length=256, blank=True, null=True)
    profession_type = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.profession_name + self.profession_hot

    def __lt__(self, other):
        return int(self.profession_hot) > int(other.profession_hot)

    class Meta:
        ordering = ["id"]
        verbose_name = "专业信息"
        verbose_name_plural = "专业信息"


