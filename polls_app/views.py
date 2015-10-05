from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import RequestContext, loader
from django.shortcuts import render_to_response

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    output = ', '.join([p.question_text for p in latest_question_list])

    # template = loader.get_template('polls_app/index.html')
    # context = RequestContext(request, {
    #     'latest_question_list': latest_question_list,
    # })
    # return HttpResponse(template.render(context))

    return render_to_response('polls_app/index.html',
                                {'latest_question_list': latest_question_list,}
    )

def detail(request, question_id):
    return HttpResponse("Your're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

# def index(request):
#    return render(request, "Hello, world. You're at the polls index.")

