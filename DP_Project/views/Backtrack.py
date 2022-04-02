from django.http import JsonResponse
from DP_Project.models.knapsack import Knapsack


def Backtrack(request):
    knapsacks = Knapsack.objects.filter(number='1')

    v_list = []  # 体积列表
    w_list = []  # 价值列表

    v_list.append(0)  # 体积列表初始化
    w_list.append(0)  # 价值列表初始化

    for knapsack in knapsacks:
        v_list.append(int(knapsack.volume))
        w_list.append(int(knapsack.worth))

    V = 200
    N = len(v_list)
    f = [0] * (V + 1)

    for i in range(1, N):
        for j in range(V, v_list[i] - 1, -1):
            f[j] = max(f[j], f[j - v_list[i]] + w_list[i])

    maxvalue = f[V]

    return JsonResponse({
        'result': 'success',
        'maxvalue': maxvalue,
    })
