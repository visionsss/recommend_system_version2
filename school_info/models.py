from django.db import models


class School_info(models.Model):
    school_name = models.CharField(max_length=256)
    school_rank = models.CharField(blank=True, max_length=256)
    school_province = models.CharField(max_length=256)
    school_city = models.CharField(max_length=256)
    type_985 = models.CharField(max_length=256)
    type_211 = models.CharField(max_length=256)
    type_self = models.CharField(max_length=256)
    school_belong = models.CharField(max_length=256)
    school_type1 = models.CharField(max_length=256)
    school_type2 = models.CharField(max_length=256)


