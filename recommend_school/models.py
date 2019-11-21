from django.db import models


class re_school(models.Model):
    school_name = models.CharField(max_length=128)
    school_province = models.CharField(max_length=128)
    student_type = models.CharField(max_length=128)
    year = models.CharField(max_length=128)
    epoch = models.CharField(max_length=128)
    score_avg = models.IntegerField()
    score_low = models.IntegerField()
    score_province = models.IntegerField()

    def __str__(self):
        return self.school_name

    class Meta:
        ordering = ["id"]
        verbose_name = "专业信息"
        verbose_name_plural = "专业信息"
