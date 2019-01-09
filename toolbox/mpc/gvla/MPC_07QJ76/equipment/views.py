from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

from .models import Equipment
#from .forms import ProjectForm
#from pages.models import Page

class EquipmentList(ListView):
	model = Equipment
	context_object_name = 'equipment'

	def get_context_data(self, **kwargs):
		context = super(EquipmentList, self).get_context_data(**kwargs)
		context['equipment'] = Equipment.objects.all()
		return context