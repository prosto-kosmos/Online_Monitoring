from django.db import models

class Data(models.Model):
    datetime = models.CharField(primary_key=True, max_length=20)
    open_pos_yur_long = models.IntegerField()
    open_pos_yur_short = models.IntegerField()
    open_pos_fiz_long = models.IntegerField()
    open_pos_fiz_short = models.IntegerField()
    open_pos_all = models.IntegerField()
    number_persons_yur_long = models.IntegerField()
    number_persons_yur_short = models.IntegerField()
    number_persons_fiz_long = models.IntegerField()
    number_persons_fiz_short = models.IntegerField()
    number_persons_all = models.IntegerField()
    close = models.FloatField(null=True)
    capacity_control = models.IntegerField(null=True)
    open_pos_control = models.IntegerField(null=True)
    short_code = models.CharField(max_length=10, null=True)
