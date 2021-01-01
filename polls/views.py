from django.shortcuts import render
from django.http import Http404, HttpResponse, request
from .models import Question
from django.template import loader

# Create your views here.
def index(request):
  latest_question_list = Question.objects.order_by('-pub_date')[:5]
  context = {'latest_question_list': latest_question_list}
  return render(request, 'polls/index.html', context)

def details(req, q_id):
  try:
    question = Question.objects.get(pk=q_id)
    return HttpResponse("You're looking at question: %s" % q_id)
  except Question.DoesNotExist:
    raise Http404('Question does not exist')
  return render(request, 'polls/details.html', {'question': question})

def result(req, q_id):
  res = "You're looking at question: %s."
  return HttpResponse(res % q_id)

def vote(req, q_id):
  return HttpResponse("You're voting on question %s" % q_id)