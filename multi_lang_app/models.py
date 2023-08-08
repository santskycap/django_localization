# general imports
from __future__ import unicode_literals
import uuid

# django imports
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
# from django.utils.translation import ugettext_lazy as _
from django.utils.translation import gettext_lazy as _


# local imports
from utils.managers import UserManager
from utils.basemodel import BaseModel

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
	'''
		User model with username as username field
	'''
	username = models.CharField(
		_('username'),
		max_length=256,
		unique=True,
		blank=True,
		null=True
	)
	email = models.EmailField(
		_('email address'),
		unique=False,
		blank=True,
		null=True
	)
	first_name = models.CharField(
		_('first_name'),
		max_length=256,
		blank=True,
		null=True
	)
	last_name = models.CharField(
		_('last_name'),
		max_length=256,
		blank=True,
		null=True
	)
	full_name = models.TextField(
		_('full_name'),
		blank=True,
		null=True
	)
	is_active = models.BooleanField(
		_('active status'),
		help_text="Indicates if user is verified either by phone Or email",
		default=False
	)
	is_staff = models.BooleanField(
		_('staff status'),
		default=False
	)
	is_blocked = models.BooleanField(
		_('blocked status'),
		help_text="Indicates if user is blocked by admin",
		default=False
	)

	objects = UserManager()

	USERNAME_FIELD = 'username'

	class Meta:
		db_table = "User"
		verbose_name = _('User')
		verbose_name_plural = _('User')

	def __str__(self):
		return f'{self.pk}'

	@property
	def get_name(self):
		name = f'{self.first_name} {self.last_name}'
		return name

