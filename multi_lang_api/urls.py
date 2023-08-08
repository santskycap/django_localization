# general imports
from __future__ import unicode_literals

# django imports
from django.urls import path

# local imports
from multi_lang_api.views import (
	LanguageAPIView,
)


urlpatterns = [
	path(
		'',
		LanguageAPIView.as_view(),
		name='lang_api_view'
	),
]

