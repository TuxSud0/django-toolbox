from django.db import models

class equip(models.Model):
	tag_no = models.CharField(primary_key=True,max_length=10)
	name = models.CharField(null=True,max_length=30,default='equipment name')
	
	def __str__(self):
		return self.tag_no

class reqpkg(models.Model):
	pkg_no = models.CharField(primary_key=True, max_length=10)
	pkg_name = models.CharField(null=True,max_length=30,default='pkg_name')
	
	def __str__(self):
		return self.tag_no	
