from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.urls import reverse
from .models import Question, Choice
"""
# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def owner(request):
    return HttpResponse("Hello, world. 5e8c8476 is the polls index.")

def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    # response = "You're looking at the results of question %s."
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
"""

# class based Generic Views
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

# owner - it's test view
def owner(request):
    return HttpResponse("Hello, world. 319d3166 is the polls index.")


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# cookie example view
def cookie(req):
    print(req.COOKIES)
    resp = HttpResponse('C is for cookie and that is good enough for me...')
    resp.set_cookie('zap', 11) # no expireation unitl browser close
    resp.set_cookie('TYJ', 23, max_age=1000) # seconds until expire
    return resp

# session example view
def sessfon(req):
    num_visits = req.session.get('num_visits',0)+1
    req.session['num_visits'] = num_visits
    if num_visits > 4: del(req.session['num_visits'])
    return HttpResponse('View count='+str(num_visits))
