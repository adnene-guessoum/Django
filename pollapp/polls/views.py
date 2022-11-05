from django.shortcuts import render
#from django.http import HttpResponse

#import our model classes
from .models import Question

#import our templates to display views
#from django.template import loader

# Create the views
def index(request):

	latest_question_list = Question.objects.order_by('-pub_date')[:5]

	#enough if directory properly namespaced
	#template = loader.get_template('polls/index.html')

	#passing the required context to be displayed by our template in the view
	context = {
			'latest_question_list': latest_question_list,
			}

	return render(request, 'polls/index.html', context)

def detail(request, question_id):
	return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):  
	response = "You're looking at the results of question %s" 
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s." % question_id)
