from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
	"""docstring for User model"""
	first_name=models.CharField(max_length=100)
	last_name=models.CharField(max_length=100)
	alias_name=models.CharField(max_length=50)
	email=models.EmailField()


"""class UserEduction(object):"""
"""docstring for UserEduction"""
	

class Skill(models.Model):
	"""docstring for Skill"""
	skill_name=models.CharField(max_length=100)


class Company(models.Model):
	"""docstring for Company"""
	company_name=models.CharField(max_length=100)
	
