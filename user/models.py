from django.db import models


# Create your models here.
class User(models.Model):
    sex_gender = (
        ('男', "男"),
        ('女', "女"),
    )
    province_gender = (
        ('广东', '广东'),
    )
    subject_gender = (
        ('理科', '理科'),
        ('文科', '文科'),
    )

    username = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    sex = models.CharField(max_length=32, choices=sex_gender, default="男")
    province = models.CharField(max_length=64, choices=province_gender, default="广东")
    subject = models.CharField(max_length=64, choices=subject_gender, default="理科")
    score = models.IntegerField(default=0)
    personality_type = models.CharField(max_length=32, default=0)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ["c_time"]
        verbose_name = "用户信息"
        verbose_name_plural = "用户信息"
