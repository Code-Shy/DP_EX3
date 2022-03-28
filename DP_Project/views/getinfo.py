from django.http import JsonResponse

from DP_Project.models.knapsack import Knapsack

def getinfo_web(request):
    knapsack = Knapsack.objects.all()[0]
    return JsonResponse({
        'result': "success",
        'volume': knapsack.volume,
        'worth': knapsack.worth,
    })


def getinfo_app(request):
    knapsack = Knapsack.objects.all()[0]
    return JsonResponse({
        'result': "success",
        'volume': knapsack.volume,
        'worth': knapsack.worth,
    })


def getinfo(request):
    platform = request.GET.get('platform')
    if platform == 'APP':
        return getinfo_app(request)
    elif platform == 'WEB':
        return getinfo_web(request)
