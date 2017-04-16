from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Tag (models.Model):
    name = models.CharField(max_length=31, unique=True)
    slug = models.SlugField(max_length=31, unique=True, help_text='A label for config.')
    
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('organizer_tag_detail', args=(self.slug,))
    
    class Meta:
        ordering = ['name']
#######################################################################################################################
class Startup (models.Model):
    name = models.CharField(max_length=31, db_index = True)
    slug = models.SlugField(max_length=31, db_index=True, help_text ='A label for URL config')
    description = models.TextField()
    fuond_date = models.DateField('date founded')
    contact = models.EmailField()
    website = models.URLField(max_length = 255)
    tags = models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('organizer_startup_detail', kwargs={'slug':self.slug})
    
    class Meta:
        ordering = ['name']
        get_latest_by = 'founded_date'
#######################################################################################################################
class NewsLink (models.Model):
    name = models.CharField(max_length=31)
    pub_date = models.DateField('date published')
    link = models.URLField(max_length=255)
    startup = models.ForeignKey(Startup)
    def __str__(self):
        return "{}:{}".format(self.startup, self.title)
    class Meta:
        verbose_name = 'news article'
        ordering = ['-pub_date']
        get_latest_by = 'pub_date'
