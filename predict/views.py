from django.shortcuts import render
from predict.forms import InputForm

from predict.predictor import stateInference

# Create your views here.


def home(request):
    form = InputForm(request.POST)
    text = None
    output = []
    if form.is_valid():
        text = form.cleaned_data['post']
    if text:
        numbers = text.split()
        output = stateInference(numbers, 50)

    context = {
        'form': form,
        'text': output,
    }
    return render(request, 'predict/home.html', context=context)
