# django_localization
Goal of localization is to allow a single web application to offer its content in multiple languages and formats tailored to the audience.

# localization (also known as internationalization)

# Enable Localization: In your settings.py
	USE_I18N = True
	USE_L10N = True

# Define Languages: In settings.py
	LANGUAGES = [
    	('en', _('English')),
    	('fr', _('French')),
    	# Add more languages here
    ]

# Define LANGUAGE_SESSION_KEY (optional), By default LANGUAGE_SESSION_KEY is 'django_language'
	LANGUAGE_SESSION_KEY = 'selected_language'

# Define LOCALE_PATHS
	LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale'),]

# Add LocaleMiddleware before CommonMiddleware
	django.middleware.locale.LocaleMiddleware

# Create message files
	python manage.py makemessages -l en
	python manage.py makemessages -l fr

	This will create a django.po file in the directory locale/en/LC_MESSAGES/ of each application.

	Only translation strings will go in django.po file.
	text = _("Hello, world!")
	Here Original String will be Msgid
	Translation string will be Msgstr which will be displayed.
	msgid "Hello, world!"
	msgstr "Bonjour, le monde!"

# After translating string compile messages by running
	python manage.py compilemessages

# To work in templates use it like this
	{% load i18n %}
	<h1>{% translate "Welcome" %}</h1>

	Here Welcome is msgid Or we can pass this from view as well by translating this way
	message = _('Welcome to our website!')

# To handle this in API views create customLanguageMiddleware
	Pass selected language in HTTP_ACCEPT_LANGUAGE header(Accept-Language) & activate this in middleware.

