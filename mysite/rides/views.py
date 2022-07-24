from webbrowser import get
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from rides.strava_api import getAthleteStat
from .models import Athlete, Activity, Choice, Question

def index(request):
    latest_athlete_list = Athlete.objects.order_by('-pub_date')[:5]
    context = {'latest_athlete_list': latest_athlete_list}
    return render(request, 'rides/index.html', context)

def detail(request, athlete_id):
    #question = get_object_or_404(Question, pk=question_id)
    athlete = get_object_or_404(Athlete, pk=athlete_id)
    return render(request, 'rides/detail.html', {'athlete': athlete})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'rides/results.html', {'question': question})

def vote(request, athlete_id):
    athlete = get_object_or_404(Athlete, pk=athlete_id)
    try:
        getAthleteStat(athlete_id)
        # selected_athlete = athlete.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'rides/detail.html', {
            'athlete': selected_athlete,
            'error_message': "You didn't select a choice.",
        })
    else:
        # selected_athlete.vote += 1
        # selected_athlete.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('rides:results', args=(athlete.id,)))

        