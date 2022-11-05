from django.urls import path
from . import views

urlpatterns = [
			# index /polls/
			path('', views.index, name='index'),
			# index /polls/5/ (for question_id 5)
			path('<int:question_id>/', views.detail, name='detail'),
			# index /polls/5/results/
			path('<int:question_id>/results/', views.results, name='results'),
			# index /polls/5/vote/
			path('<int:question_id>/vote/', views.vote, name='vote'),
		]
