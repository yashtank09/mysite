from django.urls import path

from .views import IndexView, owner, DetailView, ResultsView, vote, cookie, sessfon

app_name = 'polls'
urlpatterns = [

    # ex: /polls/
    path('', IndexView.as_view(), name='index'),

    # polls/owner
    path('owner', owner, name='owner'),

    # ex: /polls/5/
    # the 'name' value as called by the {% url %} template tag
    path('<int:pk>/', DetailView.as_view(), name='detail'),

    # ex: /polls/5/results/
    path('<int:pk>/results/', ResultsView.as_view(), name='results'),

    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', vote, name='vote'),

    # ex: cookie
    path('cookie/', cookie, name='cookie'),

    # ex: cookie
    path('session/', sessfon, name='seesfon'),
]