from django.db import models



class Note(models.Model):
    seq = models.IntegerField(default=0)
    subject = models.CharField(max_length=200)
    detail = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.subject


class Note002(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    detail = models.TextField(null=True, blank=True)

class Wk(models.Model):
    yr = models.IntegerField()
    num = models.IntegerField()
    date1 = models.DateField('Date From')
    date2 = models.DateField('Date To')
    # Accroding to https://www.epochconverter.com/weeks/2019
    # Week 01	December 31, 2018	January 6, 2019


class Work(models.Model):
    date1 = models.DateField('用工日期')
    place = models.CharField('用工地點',max_length=200,default="")
    worker = models.IntegerField('工人編號')
    thing = models.CharField('工作內容', max_length=200,default="")

    def __str__(self):
        return self.place
        return self.thing


#place = models.CharField(max_length=200,verbose_name=u"請寫下工作地點",default="")
