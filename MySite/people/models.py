# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class blog(models.Model):
   name = models.CharField(max_length = 100)
   tagline = models.TextField()
   
   def __unicode__(self):
      return self.name
      
class Author(models.Model):
   name = models.CharField(max_length = 50)
   email = models.EmailField()
   
   def __unicode__(self):
      return self.name
      

   