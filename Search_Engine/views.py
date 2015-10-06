from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, render_to_response
from django.template.context_processors import csrf
from Search_Engine.models import Key_Words
from django.utils import timezone

def home_page(request):
    c = {}
    c.update(csrf(request))
    return render_to_response("Search_Engine/home_page.html", c)
#def home_page(request):
#    return render(request, 'mysite/home_page.html')

def find(request):
	if(request.POST['key_word'] == ""):
		return HttpResponseRedirect('/')
	else:
		kw = Key_Words(text = request.POST['key_word'], pub_date = timezone.now())
		kw.save()
		kws = Key_Words.objects.order_by('-pub_date')
		return render(request, 'Search_Engine/find.html', {'kws':kws})
# Create your views here.
