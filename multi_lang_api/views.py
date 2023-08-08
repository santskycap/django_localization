# general imports
from __future__ import unicode_literals

# django imprts
from django.utils.translation import activate, get_language, gettext as _

# django rest imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.


class LanguageAPIView(APIView):

	def post(self, request, *args, **kwargs):
		other_msg = ('This is non translational message!')
		try:
			return_msg = _('This is API response!')

			return_data = {
				"status": 200,
				"message": return_msg,
				"non_trans": other_msg
			}
			return Response(return_data,status=200)

		except Exception as e:
			return_msg = str(e)
			return_data = {
				"status": 400,
				"message": return_msg,
				"non_trans": other_msg
			}
			return Response(return_data,status=400)

