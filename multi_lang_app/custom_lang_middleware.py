from django.conf import settings

from django.utils import translation

class SetLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if 'api' in request.META.get("PATH_INFO"):
            language_code = request.META.get('HTTP_ACCEPT_LANGUAGE') or settings.LANGUAGE_CODE
            translation.activate(language_code)
            response = self.get_response(request)
            translation.deactivate()
        else:
            response = self.get_response(request)
        return response

