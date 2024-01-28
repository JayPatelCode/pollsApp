from django.urls import path
from .views import *
app_name="polls"

# urlpatterns = [
#     path("",index,name='index'),

#     #polls/5/
#     path("<int:question_id>/",detail,name="detail"),
#     #polls/5/results/
#     path("<int:question_id>/results/",results,name="results"),
#     #polls/5/vote/
#     path("<int:question_id>/vote/",vote,name="vote"),
    
# ]


urlpatterns = [
    path("",IndexView.as_view(),name='index'),

    #polls/5/
    path("<int:pk>/",DetailView.as_view(),name="detail"),
    #polls/5/results/
    path("<int:pk>/results/",ResultsView.as_view(),name="results"),
    #polls/5/vote/
    path("<int:question_id>/vote/",vote,name="vote"),
    
]

