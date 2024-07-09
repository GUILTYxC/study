from django import forms
from django.shortcuts import render
from myadmin.models import Card
import random
import string

class CardGenerateForm(forms.Form):
    duration = forms.IntegerField(label='有效期（天）', min_value=1)
    count = forms.IntegerField(label='数量', min_value=1)
    remark = forms.CharField(label='备注', max_length=200, required=False)

def generate_card(request):
    generated_cards = []  # 用于存储生成的卡密

    if request.method == 'POST':
        form = CardGenerateForm(request.POST)
        if form.is_valid():
            duration = form.cleaned_data['duration']
            count = form.cleaned_data['count']
            remark = form.cleaned_data['remark']

            for _ in range(count):
                unique = False
                while not unique:
                    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
                    if not Card.objects.filter(code=code).exists():
                        unique = True
                try:
                    card = Card.objects.create(code=code, duration=duration, remark=remark)
                    generated_cards.append(card)  # 将生成的卡密添加到列表中
                except Exception as e:
                    print(f"Error when creating card: {e}")

    else:
        form = CardGenerateForm()

    context = {
        'form': form,
        'generated_cards': generated_cards  # 将生成的卡密传递给模板
    }
    return render(request, 'myadmin/card/index.html', context)
