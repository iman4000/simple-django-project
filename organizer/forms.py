from django import forms
from django.core.exceptions import ValidationError

from .models import Tag, Startup, NewsLink


class SlugCleanMixin:
	def clean_slug(self):
		new_slug = (self.cleaned_data['slug'].lower())
		if new_slug =='create':
			raise ValidationError('slug may not be "create"')
		return new_slug

class NewsLinkForm (SlugCleanMixin, forms.ModelForm):
	class Meta:
		model = NewsLink
		fields = '__all__'

class StartupForm (SlugCleanMixin, forms.ModelForm):
	class Meta:
		model = Startup
		fields = '__all__'

class TagForm(SlugCleanMixin, forms.ModelForm):
	
	class Meta:
		model = Tag
		fields = '__all__'
	
	def clean_name(self):
		return self.cleaned_data['name'].lower()

