from django.db import models
from django.core.urlresolvers import reverse

from embed_video.fields import EmbedVideoField


class Technique(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    video = EmbedVideoField(verbose_name='My video',
                            help_text='This is a help text')

    def __unicode__(self):
        return self.title


    def __unicode__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('technique:detail', kwargs={'pk': self.pk})
