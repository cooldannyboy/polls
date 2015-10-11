from django.http import HttpResponseRedirect
from .models import Question, Choice
from django.shortcuts import render_to_response, render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.db.models import Count

class IndexView(generic.ListView):
    template_name = 'polls_app/index.html'
    context_object_name  = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions. (not including those
        set to be published in the future)"""
        # return Question.objects.order_by('-pub_date')[:5]

        # q = Question.objects.annotate(num_choice=Count('choice'))

        # return Question.objects.filter(
        #     pub_date__lte=timezone.now()
        # ).order_by('-pub_date')[:5]

        return Question.objects.annotate(
             choice_count=Count('choice')
         ).filter(choice_count__gte=1).filter(
             pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls_app/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        :return:
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls_app/results.html'

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
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls_app:results', args=(p.id,)))


    # return HttpResponse("You're voting on question %s." % question_id)

# def index(request):
#    return render(request, "Hello, world. You're at the polls index.")

