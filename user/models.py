from django.db import models


# Create your models here.
class User(models.Model):
    sex_gender = (
        ('male', "男"),
        ('female', "女"),
    )
    province_gender = (
        ('GuangDong', '广东'),
    )
    subject_gender = (
        ('science', '理科'),
        ('art', '文科'),
    )

    username = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    sex = models.CharField(max_length=32, choices=sex_gender, default="male")
    province = models.CharField(max_length=64, choices=province_gender, default="GuangDong")
    subject = models.CharField(max_length=64, choices=subject_gender, default="science")
    score = models.IntegerField(default=0)
    personality_type = models.CharField(max_length=32, default=0)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ["c_time"]
        verbose_name = "用户信息"
        verbose_name_plural = "用户信息"
