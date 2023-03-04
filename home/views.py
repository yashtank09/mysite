from django.views import generic
from django.http import HttpResponse

# Create your views here.
class TemplateView(generic.TemplateView):
    template_name = 'home/main.html'

def myview(req):
    print(req.COOKIES)
    num_visits = req.session.get('num_visits',0)+1
    req.session['num_visits'] = num_visits
    resp = HttpResponse('view count='+str(num_visits))
    if num_visits > 4: del(req.session['num_visits'])
    resp.set_cookie('dj4e_cookie', '319d3166', max_age=1000)
    return resp