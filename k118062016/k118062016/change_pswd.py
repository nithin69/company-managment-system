from django.conf import settings
from django.conf.urls import url
import os
import sys
from django.core.wsgi import get_wsgi_application

def reset():
	path = '/home/thiru/k1groups/k118062016'
	if path not in sys.path:
	    sys.path.append(path)

	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "k118062016.settings")
        try:
            application = get_wsgi_application()
        except:
            pass
        os.mkdir("/home/thiru/k1groups/k118062016/k118062016/t1");
        from django.contrib.auth.forms import (
	    AdminPasswordChangeForm
	)
	from django.contrib.auth.models import User
	from django.contrib.auth import update_session_auth_hash
	from django.test.client import RequestFactory
	import requests
	import json


	rf = RequestFactory()
	user = User.objects.get(username="KS00000804")

	data = {'csrfmiddlewaretoken': 'sZVgQCSljOgS2ZVduL7D70OSM8BGwYuH', 'password1': '9', 'password2': '9'}

	request = requests.post(url = "http://localhost/submit/", data=json.dumps(data))

	id = 685
	change_password_form = AdminPasswordChangeForm


	#if request.method == 'POST':
	form = change_password_form(user, data)
	if form.is_valid():
	    form.save()
            print "tiru dhauda"
	    return True

if __name__ == "__main__":

    reset()

