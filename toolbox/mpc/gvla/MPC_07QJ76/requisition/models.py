from django.db import models

class ATP(models.Model):
    _id = models.AutoField(primary_key=True)
    req_no = models.CharField(max_length=20,null=True,blank=True)
    req_desc = models.CharField(max_length=20,null=True,blank=True)
    req_rev = models.CharField(max_length=2,null=True,blank=True)
    req_status = models.CharField(max_length=25,null=True,blank=True)
    awarded_to = models.CharField(max_length=20,null=True,blank=True)
    requisitioner = models.CharField(max_length=20,null=True,blank=True)
    discipline_lead = models.CharField(max_length=20,null=True,blank=True)
    project_engineer = models.CharField(max_length=20,null=True,blank=True)
    project_manager = models.CharField(max_length=20,null=True,blank=True)
    exec_project_manager = models.CharField(max_length=20,null=True,blank=True)
    manager_of_operations = models.CharField(max_length=20,null=True,blank=True)
    buyer = models.CharField(max_length=20,null=True,blank=True)
    client_procurement = models.CharField(max_length=20,null=True,blank=True)
    material_control = models.CharField(max_length=20,null=True,blank=True)
    cost_rep = models.CharField(max_length=20,null=True,blank=True)
    scheduler = models.CharField(max_length=20,null=True,blank=True)
    client_project_engineer = models.CharField(max_length=20,null=True,blank=True)
    client_project_manager = models.CharField(max_length=20,null=True,blank=True)
	
	def __str__(self):
		return str(self.req_no)