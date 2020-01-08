from django.db import models


class School_info(models.Model):
    school_name = models.CharField(max_length=256)
    school_rank = models.CharField(blank=True, max_length=256)
    school_province = models.CharField(max_length=256)
    school_city = models.CharField(max_length=256)
    type_985 = models.CharField(max_length=256)
    type_211 = models.CharField(max_length=256)
    type_self = models.CharField(max_length=256)
    student_type = models.CharField(max_length=256)
    epoch = models.CharField(max_length=256)    # 批次
    lowest_score = models.CharField(max_length=256)

    def __lt__(self, other):
        return self.lowest_score > other.lowest_score

    def __str__(self):
        return self.school_name

    class Meta:
        ordering = ["id"]
        verbose_name = "学校基本信息"
        verbose_name_plural = "学校基本信息"


class One_School(models.Model):
    school_name = models.CharField(max_length=256)
    profession_name = models.CharField(max_length=256)
    student_type = models.CharField(max_length=256)
    year = models.CharField(max_length=256)
    top_score = models.CharField(max_length=256)
    avg_score = models.CharField(max_length=256)
    lowest_score = models.CharField(max_length=256)
    lowest_rank = models.CharField(max_length=256)
    epoch = models.CharField(max_length=256)
    pictures = models.ImageField(upload_to='img')

    def __str__(self):
        return self.school_name

    class Meta:
        ordering = ["id"]
        verbose_name = "学校详细信息"
        verbose_name_plural = "学校详细信息"


class school_score(models.Model):
    school_name = models.CharField(max_length=256)
    score = models.CharField(max_length=256)

    def __str__(self):
        return self.school_name + self.score

    class Meta:
        ordering = ["id"]
        verbose_name = "学校分数"
        verbose_name_plural = "学校分数"
