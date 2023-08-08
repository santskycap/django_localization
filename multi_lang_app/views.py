from django.conf import settings
from django.shortcuts import render
from django.utils.translation import activate, get_language, gettext as _
from django.http import HttpResponseRedirect

# Create your views here.


def set_language(request, language_code):
	# Set the language preference for the current user
	
	response = HttpResponseRedirect(request.META.get('HTTP_REFERER'))

	# Store the language preference in the user's session
	# request.session['django_language'] = language_code
	# request.session[settings.LANGUAGE_SESSION_KEY] = language_code
	response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language_code)
	
	return response


def home(request):
    # Translating text in Python code
    message = _('Welcome to our website!')

    return render(request, 'my_template.html', {'message': message})

