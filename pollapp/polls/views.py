from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

# Create the views
def index(request):

	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	#passing the required context to be displayed by our template in the view
	context = {
			'latest_question_list': latest_question_list,
			}

	return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):  
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# display the form again
		return render(request, 'polls/detail.html', {'question':question,
			'error_message': "You didn't select a choice.",})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		#Best practice: always return an HttpResponseRedirect after successfull
		#post data to prevent posting twice on back button 
	return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))




'''
#other 404 option to reduce code
def detail(request, question_id):
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	return render(request, 'polls/detail.html', {'question':question})
'''

