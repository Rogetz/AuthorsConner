from django.shortcuts import render
import datetime


def current_datetime(request):
    now = datetime.datetime.now()
    return render(request,'current_datetime.html', {'current_date': now})


def hour_offset(request, direction="plus", hours=5):
    offset = int(hours)
    dt = 00
    if direction == 'plus':
        dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    else:
        dt = datetime.datetime.now() - datetime.timedelta(hours=offset)
    return render(request,'hours_offset.html', {'offset_date': dt})

# always give the parameters default values for them to work well
def name_display(request,name="Tony"):
    finalName = name
    return render(request,'name_display.html', {'name': finalName})
