from django.db import models
from myadmin.models import User
import os
from myxuexi import settings
from django.utils import timezone


class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    daily_new_words = models.IntegerField(default=20)  # 每天新学习的单词数量
    daily_review_words = models.IntegerField(default=20)  # 每天复习的单词数量
    study_by_frequency = models.BooleanField(default=True)  # 是否按词频背诵
    last_new_word_fetch_date = models.DateField(null=True, blank=True)
    last_page = models.IntegerField(default=1)  # 用户最后所在的页码

    def __str__(self):
        return f"{self.user.username}'s settings"

    def update_last_new_word_fetch_date(self):
        self.last_new_word_fetch_date = timezone.now().date()
        self.save()

    class Meta:
        db_table = 'usersettings'



class Cet4Word(models.Model):
    frequency = models.IntegerField(default=0)
    word = models.CharField(max_length=100, unique=True)
    phonetic = models.CharField(max_length=255, blank=True, null=True)
    translation = models.TextField(blank=True, null=True)
    # 发音字段保留空，但可以通过方法获取

    def get_audio_url(self):
        first_letter = self.word[0].lower()  # 获取单词首字母并转换为小写
        audio_file = self.word + '.wav'
        # 构建音频文件的路径
        return os.path.join(settings.STATIC_URL, 'fayin', 'Lingoes English', 'voice', first_letter, audio_file)

    class Meta:
        db_table = 'cet4word'

class UserWord_cet4(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    word = models.ForeignKey(Cet4Word, on_delete=models.CASCADE)
    mastery_level = models.CharField(max_length=10, choices=[('mastered', 'Mastered'), ('familiar', 'Familiar'), ('unknown', 'Unknown')])
    last_reviewed = models.DateField(auto_now=True)  # 最后一次复习日期
    familiar_count = models.IntegerField(default=0)  # 连续被标记为“熟悉”的次数

    def __str__(self):
        return f"{self.user.username} - {self.word.word}"

    class Meta:
        db_table = 'userword_cet4'