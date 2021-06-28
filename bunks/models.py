from django.db import models
from django.utils import timezone 

import datetime 

# Create your models here.


# bunk: from_user, to_user, time

# user: username, photo (both strings)

class User(models.Model):
	username = models.CharField(max_length=20)
	photo = models.CharField(max_length=300)
	def __str__(self):
		return self.username
	def setPhoto(self, photo):
		self.photo = photo 

class Bunk(models.Model):
	from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='outgoing_bunk')
	to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='incoming_bunk')
	bunk_time = models.DateTimeField('date bunked')
	def __str__(self):
		#return f'from {self.from_user.username} to {self.to_user.username} at {self.bunk_time.time}, {self.bunk_time.date}'
		return 'from {} to {} at {}, {}'.format(self.from_user.username, self.to_user.username, self.bunk_time.time().strftime('%H:%M:%S'), self.bunk_time.date())
		#return "from " + self.from_user.username + " to " + self.to_user.username + " at " + self.bunk_time.strftime()
	def bunked_recently(self):
		return timezone.now() - datetime.timedelta(days=1) <= self.bunk_time <= timezone.now()