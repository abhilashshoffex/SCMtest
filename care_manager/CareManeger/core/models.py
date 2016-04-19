from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Registration(models.Model):
	full_name = models.CharField(max_length=120)
	contact = models.CharField(max_length=12)


	def __unicode__(self):
		return self.full_name