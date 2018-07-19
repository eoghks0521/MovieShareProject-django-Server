import datetime

from django.db import models
from django.utils import timezone
from django.conf import settings





class Client(models.Model):

	clientid = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.clientid

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

