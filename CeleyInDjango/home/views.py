from django.shortcuts import render, redirect, get_object_or_404
from .forms import NumberForm
from .models import Number
from .tasks import adding


# Create your views here.
def home(request):
    numbers = Number.objects.all()
    if request.method == 'POST':
        form = NumberForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            number = Number(x=cd['x'], y=cd['y'])
            number.save()
            result = adding.delay(cd['x'], cd['y'], number.id)
            number.task_id = result.id
            number.save()
            return redirect('home:home')
    else:
        form = NumberForm()
    return render(request, 'home/home.html', {'form': form, 'numbers': numbers})


def sum(request, num_id):
    numbers = Number.objects.get(id=num_id)
    return render(request, 'home/sum.html', {'numbers': numbers})
