from django.db import models

class Data(models.Model):
    class Meta: 
        unique_together = ('datetime', 'code') 
    datetime = models.CharField(max_length=20)
    code = models.CharField(max_length=6)
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
