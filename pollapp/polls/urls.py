from django.urls import path
from . import views

# namespace to the urlconf to differentiate in cases of multiple, similarly
# named templates/views in different apps inside the same django project
app_name = 'polls'
urlpatterns = [
		path('', views.IndexView.as_view(), name='index'),
		path('<int:pk>/', views.DetailView.as_view(), name='detail'),
		path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
		path('<int:question_id>/vote/', views.vote, name='vote'),
		]
