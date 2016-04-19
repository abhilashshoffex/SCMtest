from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
import urllib2
import urllib
# Create your views here.
from .models import Registration



def index(request):
	return render(request, "core/index.html", {})

def sendSMS(uname, hashCode, numbers, sender, message):
    data =  urllib.urlencode({'username': uname, 'hash': hashCode, 'numbers': numbers,
        'message' : message, 'sender': sender})
    data = data.encode('utf-8')
    request = urllib2.Request("http://api.textlocal.in/send/?")
    f = urllib2.urlopen(request, data)
    fr = f.read()
    return(fr)

def submited(request):
	context = {}
	if request.method == 'POST':
		name = request.POST.get('name')
		mob = request.POST.get('mobile')

		if mob:
			register = Registration.objects.filter(contact=mob).count()

			if register > 0:
				context['error'] = 'yes'
				return render(request, "core/index.html", context)
			else:
				entry = Registration(
					full_name = name, 
					contact = mob
					)
				entry.save();
				msg = "Thank You For registration in SCPMR, our team will contact you shortly. \n www.shoffex.com"
				sendSMS('sotari.biz@gmail.com', 'da1e1331d30c4dcff5a4780b52fa9fb327764bb1', mob , 'TXTLCL', msg)
				return render(request, "core/submited.html", {})

	return HttpResponseRedirect('/')
