from django.db import models

class Key_Words(models.Model):
	text = models.CharField(max_length = 128)
	pub_date = models.DateTimeField('date published')
	def __str__(self):              # __unicode__ on Python 2
		return self.text
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
# Create your models here.
