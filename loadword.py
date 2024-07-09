import xlrd
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myxuexi.settings')
django.setup()

from mybei.models import Cet4Word

def import_data_from_xls(xls_path):
    workbook = xlrd.open_workbook(xls_path)
    sheet = workbook.sheet_by_index(0)

    for row_idx in range(1, sheet.nrows):  # 从1开始，假设第一行是表头
        frequency, word, phonetic, translation = sheet.row_values(row_idx)[:4]

        cet4_word, created = Cet4Word.objects.get_or_create(
            word=word.strip(),
            defaults={
                'frequency': int(frequency) if frequency else 0,
                'phonetic': phonetic.strip() if phonetic else '',
                'translation': translation.strip() if translation else ''
            }
        )

        if not created:
            # 如果单词已经存在，更新其信息
            cet4_word.frequency = int(frequency) if frequency else 0
            cet4_word.phonetic = phonetic.strip() if phonetic else ''
            cet4_word.translation = translation.strip() if translation else ''
            cet4_word.save()

# 调用函数
xls_path = 'cet4.xls'  # 修改为你的xls文件路径
import_data_from_xls(xls_path)
