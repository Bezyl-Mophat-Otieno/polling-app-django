from django.shortcuts import render
from .models import Question , Choice
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.urls import reverse
from django.shortcuts import render,get_object_or_404
#This is where all the app logic goes ie The Controller.
# Create your views here.

'''Get questions and display them'''

latest_question_list = Question.objects.order_by('-pub_date')[:5]
context = {'latest_question_list':latest_question_list}

def index(request):
    return render(request,'polls/index.html',context)
'''Get additionall more information about a question and its choices '''

def details (request , question_id):
    try:
      question= Question.objects.get(pk=question_id)
      context = {'question':question}
    except Question.DoesNotExist:
       raise Http404('Question not found')
    return render(request,'polls/details.html',context)

'''Get Question and display results'''

def results (request , question_id):
   question = get_object_or_404(Question , pk=question_id)
   context = {'question': question}
   return render(request,'polls/results.html',context)

'''Vote for a question'''

# Vote for a question choice
def votes(request, question_id):
    # print(request.POST['choice'])
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
      
      

            
