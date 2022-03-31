from django.http import JsonResponse
from DP_Project.models.knapsack import Knapsack


def getinfo(request):
    knapsack = Knapsack.objects.all()[0]
    return JsonResponse({
        'result': "success",
        'volume': knapsack.volume,
        'worth': knapsack.worth,
    })
