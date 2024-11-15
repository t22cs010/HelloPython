from django.shortcuts import render

# Create your views here.
from .models import Schedule
from .forms import ScheduleForm

def schedule_list(request):
    schedules = Schedule.objects.all().order_by('day')
    return render(request, 'schedule_list.html', {'schedules': schedules})

def add_schedule(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('schedule_list')
    else:
        form = ScheduleForm()
    return render(request, 'add_schedule.html', {'form': form})