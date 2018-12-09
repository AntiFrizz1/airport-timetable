from django.shortcuts import render
import data.database
# Create your views here.


def index(request):
    arrival = data.database.get_timetable()
    return render(request, 'timetable/html/timetable.html', {'data': arrival})
