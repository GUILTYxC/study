from django.http import JsonResponse
from django.shortcuts import render
from myapp.models import Year

def index(request):
    years = Year.objects.all().order_by('name')
    return render(request, 'myapp/zhuci.html', {'years': years})

def dropdown_selection(request):
    if request.is_ajax() and request.method == "POST":
        selected_year = request.POST.get('selectedYear', None)
        selected_type = request.POST.get('selectedType', None)
        if selected_year and selected_type:
            # 处理选中的年份和题型，例如根据年份和题型筛选数据或进行其他操作
            # 返回 JSON 响应，这里仅作为示例返回选中的年份和题型
            return JsonResponse({'selected_year': selected_year, 'selected_type': selected_type})
        else:
            return JsonResponse({'error': '没有选中的年份或题型'}, status=400)
    else:
        return JsonResponse({'error': '无效请求'}, status=400)



