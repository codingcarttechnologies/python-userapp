from django.db import models


#-------------------------------------------------------------------------
#  Site User Model
#-------------------------------------------------------------------------
class SiteUser(models.Model):
    username = models.CharField(max_length=140)
    birthday = models.CharField(max_length=2000)
    eligible = models.CharField(max_length=2000)
    random_number = models.IntegerField()
    bizz_fuzz= models.CharField(max_length=140)

    def __unicode__(self):
        return self.username



 