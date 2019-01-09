from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

from .models import ATP
#from .forms import ProjectForm
#from pages.models import Page

'''
from django.http import HttpResponse
from django.template import loader

def my_view(request):
    # View code here...
    t = loader.get_template('/requistion/atp.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request), content_type='application/xhtml+xml')
'''
'''
render()
render(request, template_name, context=None, content_type=None, status=None, using=None
'''

'''
class ATP_View(ListView):
	model = ATP
	context_object_name = 'atp'

	def get_context_data(self, **kwargs):
		context = super(ATP_View, self).get_context_data(**kwargs)
		context['atp'] = Equipment.objects.all()
		return context
'''