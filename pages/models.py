from django.db import models

class Page(models.Model):
	id = models.IntegerField(primary_key=True)
	title = models.CharField(max_length=120)
	content = models.TextField()
	last_update = models.DateTimeField(auto_now_add=False)


	def get_absolute_url(self):
		return "/detail/%i" % self.id