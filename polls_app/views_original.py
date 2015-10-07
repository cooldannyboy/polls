from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.template import RequestContext, loader
from django.shortcuts import render_to_response, render, get_object_or_404
from django.http import Http404
from django.core.urlresolvers import reverse

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    output = ', '.join([p.question_text for p in latest_question_list])

    # method 1
    # template = loader.get_template('polls_app/index.html')
    # context = RequestContext(request, {
    #     'latest_question_list': latest_question_list,
    # })
    # return HttpResponse(template.render(context))

    # method 2
    #return render_to_response('polls_app/index.html',
                                # {'latest_question_list': latest_question_list,}
    # )

    # method 3
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls_app/index.html', context)


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls_app/detail.html', {'question': question})

def results(request, question_id):
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls_app/results.html', {'question': question})


def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls_app/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1;
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls_app:results', args=(p.id,)))


    # return HttpResponse("You're voting on question %s." % question_id)

# def index(request):
#    return render(request, "Hello, world. You're at the polls index.")

