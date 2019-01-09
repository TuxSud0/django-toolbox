from django import forms
from django.forms import ModelForm
from .models import Equipment

class EquipmentForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Equipment
        fields = [
            'tag', 'name',
            ]

'''
from django import forms
from django.forms import ModelForm
from django.forms import ModelForm source
class ModelForm(six.with_metaclass(ModelFormMetaclass, BaseModelForm)):
    pass


def modelform_factory(model, form=ModelForm, fields=None, exclude=None,
                      formfield_callback=None, widgets=None, localized_fields=None,
                      labels=None, help_texts=None, error_messages=None,
                      field_classes=None):
    """
    Returns a ModelForm containing form fields for the given model.

    ``fields`` is an optional list of field names. If provided, only the named
    fields will be included in the returned fields. If omitted or '__all__',
    all fields will be used.

    ``exclude`` is an optional list of field names. If provided, the named
    fields will be excluded from the returned fields, even if they are listed
    in the ``fields`` argument.

    ``widgets`` is a dictionary of model field names mapped to a widget.

    ``localized_fields`` is a list of names of fields which should be localized.

    ``formfield_callback`` is a callable that takes a model field and returns
    a form field.

    ``labels`` is a dictionary of model field names mapped to a label.

    ``help_texts`` is a dictionary of model field names mapped to a help text.

    ``error_messages`` is a dictionary of model field names mapped to a
    dictionary of error messages.

    ``field_classes`` is a dictionary of model field names mapped to a form
    field class.
    """
    # Create the inner Meta class. FIXME: ideally, we should be able to
    # construct a ModelForm without creating and passing in a temporary
    # inner class.

    # Build up a list of attributes that the Meta object will have.
    attrs = {'model': model}
    if fields is not None:
        attrs['fields'] = fields
    if exclude is not None:
        attrs['exclude'] = exclude
    if widgets is not None:
        attrs['widgets'] = widgets
    if localized_fields is not None:
        attrs['localized_fields'] = localized_fields
    if labels is not None:
        attrs['labels'] = labels
    if help_texts is not None:
        attrs['help_texts'] = help_texts
    if error_messages is not None:
        attrs['error_messages'] = error_messages
    if field_classes is not None:
        attrs['field_classes'] = field_classes

from .models import Project

class ProjectForm(ModelForm):
    #required_css_class = 'required'
    class Meta:
        model = Project
        fields = [
            'name','number', 'client', 'location',
        ]
'''