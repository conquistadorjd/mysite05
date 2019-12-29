from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Question, Choice

def first(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def second(request):
    return render(request, 'polls/second.html')

def third(request):
    return render(request, 'polls/third.html')

def fourth(request):
    return render(request, 'polls/fourth.html')

def fifth(request):
    return render(request, 'polls/fifth.html')

def sixth(request):
    return render(request, 'polls/sixth.html')

def seventh(request):
    context = Question.objects.all()
    return render(request, 'polls/seventh.html',{'context':context})

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