from django.shortcuts import render, redirect
from .forms import InputNameForm
from .models import InputModel
import json


def index(request):
    if request.method == 'POST':
        form = InputNameForm(request.POST)
        if form.is_valid():
            name_input = form.cleaned_data['name']
            data = json.dumps(name_input, ensure_ascii=False)
            InputModel.objects.create(data=data, field='name')

            for count in range(1, len(request.POST) - 1):
                query = 'name' + str(count)
                input_value = request.POST[query]
                if input_value:
                    data = json.dumps(input_value, ensure_ascii=False)
                    field = json.dumps(query)
                    InputModel.objects.create(data=data, field=field)
                count += 1
        return redirect('/output/')
    else:
        form = InputNameForm()
    return render(request, 'index.html', {'form': form})


def output(request):
    data = InputModel.objects.all()
    json_list = list(data)
    return render(request, 'output.html', {'json_list': json_list})