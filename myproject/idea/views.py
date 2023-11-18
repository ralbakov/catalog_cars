from django.shortcuts import render
from django.http import HttpResponse
import logging
from .forms import CarMarkForm
from idea.models import CarModel, CarMark

logger = logging.getLogger(__name__)


def show_model_car(request):
    if request.method == 'POST':
        form = CarMarkForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            logger.info(f'Получили {name=}')
            form = CarModel.objects.filter(carmark=name)
    else:
        form = CarMarkForm()

    return render(request, 'idea/index.html', {'form': form})