from django.db import models

# Create your models here.
'''
class Page(models.Model):
	title = models.CharField(max_length=60) # The title of your page. This will be placed between <title></title> elements from your template.
	permalink = models.CharField(max_length=12, unique=True) #used to define a unique, permanent link to the URL of the page
	update_date = models.DateTimeField('Last Updated')
	bodytext = models.TextField('Page Content', blank=True) #html content to be placed in the <body> element of a template
	
	def __str__(self):
		return self.title'''
