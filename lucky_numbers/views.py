from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from random import randint
from django.http import JsonResponse
initial_run = 0

def get_lot_num():
    global initial_run
    lucky_numbers = [randint(1, 69) for _ in range(4)]
    powerball_number = randint(1, 26)
    lucky_numbers.append(powerball_number)
    data = {'lucky_numbers': lucky_numbers}
    if initial_run == 0:
        return lucky_numbers
    elif initial_run == 1:
        return JsonResponse(data)

def hello_view(request):
    global initial_run
    if initial_run == 0:
        template = get_template('lucky_numbers/index.html')
        new_numbs = get_lot_num()
        initial_run = 1
        return HttpResponse(template.render({
            'lottery_number1': new_numbs[0],
            'lottery_number2': new_numbs[1],
            'lottery_number3': new_numbs[2],
            'lottery_number4': new_numbs[3],
            'lottery_number5': new_numbs[4], 
            }))
    elif initial_run == 1:
        lucky_numbers = [randint(1, 69) for _ in range(4)]
        powerball_number = randint(1, 26)
        lucky_numbers.append(powerball_number)
        data = {'lucky_numbers': lucky_numbers}
        return JsonResponse(data)