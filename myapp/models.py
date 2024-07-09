from django.db import models
from django.utils import timezone
from myadmin.models import User
import os
from myxuexi import settings
from django.templatetags.static import static


class Stardict(models.Model):
    word = models.CharField(unique=True, max_length=100)
    sw = models.CharField(max_length=64)
    phonetic = models.CharField(max_length=255, blank=True, null=True)
    definition = models.TextField(blank=True, null=True)
    translation = models.TextField(blank=True, null=True)
    pos = models.CharField(max_length=64, blank=True, null=True)
    collins = models.SmallIntegerField(blank=True, null=True)
    oxford = models.SmallIntegerField(blank=True, null=True)
    tag = models.CharField(max_length=100, blank=True, null=True)
    bnc = models.IntegerField(blank=True, null=True)
    frq = models.IntegerField(blank=True, null=True)
    exchange = models.TextField(blank=True, null=True)
    detail = models.TextField(blank=True, null=True)
    audio = models.TextField(blank=True, null=True)

    def get_audio_url(self):
        first_letter = self.word[0].lower()  # 获取单词首字母并转换为小写
        audio_file = self.word + '.wav'
        # 构建音频文件的路径
        return os.path.join(settings.STATIC_URL, 'fayin', 'Lingoes English', 'voice', first_letter, audio_file)

    class Meta:
        managed = False
        db_table = 'stardict'


class Kydata(models.Model):
    year = models.CharField(max_length=255, blank=True, null=True)
    section_type = models.CharField(max_length=255, blank=True, null=True)
    text_content = models.TextField(blank=True, null=True)
    question_1 = models.TextField(blank=True, null=True)
    answer_1 = models.CharField(max_length=255, blank=True, null=True)
    question_2 = models.TextField(blank=True, null=True)
    answer_2 = models.CharField(max_length=255, blank=True, null=True)
    question_3 = models.TextField(blank=True, null=True)
    answer_3 = models.CharField(max_length=255, blank=True, null=True)
    question_4 = models.TextField(blank=True, null=True)
    answer_4 = models.CharField(max_length=255, blank=True, null=True)
    question_5 = models.TextField(blank=True, null=True)
    answer_5 = models.CharField(max_length=255, blank=True, null=True)
    question_6 = models.TextField(blank=True, null=True)
    answer_6 = models.CharField(max_length=255, blank=True, null=True)
    question_7 = models.TextField(blank=True, null=True)
    answer_7 = models.CharField(max_length=255, blank=True, null=True)
    question_8 = models.TextField(blank=True, null=True)
    answer_8 = models.CharField(max_length=255, blank=True, null=True)
    question_9 = models.TextField(blank=True, null=True)
    answer_9 = models.CharField(max_length=255, blank=True, null=True)
    question_10 = models.TextField(blank=True, null=True)
    answer_10 = models.CharField(max_length=255, blank=True, null=True)
    question_11 = models.TextField(blank=True, null=True)
    answer_11 = models.CharField(max_length=255, blank=True, null=True)
    question_12 = models.TextField(blank=True, null=True)
    answer_12 = models.CharField(max_length=255, blank=True, null=True)
    question_13 = models.TextField(blank=True, null=True)
    answer_13 = models.CharField(max_length=255, blank=True, null=True)
    question_14 = models.TextField(blank=True, null=True)
    answer_14 = models.CharField(max_length=255, blank=True, null=True)
    question_15 = models.TextField(blank=True, null=True)
    answer_15 = models.CharField(max_length=255, blank=True, null=True)
    question_16 = models.TextField(blank=True, null=True)
    answer_16 = models.CharField(max_length=255, blank=True, null=True)
    question_17 = models.TextField(blank=True, null=True)
    answer_17 = models.CharField(max_length=255, blank=True, null=True)
    question_18 = models.TextField(blank=True, null=True)
    answer_18 = models.CharField(max_length=255, blank=True, null=True)
    question_19 = models.TextField(blank=True, null=True)
    answer_19 = models.CharField(max_length=255, blank=True, null=True)
    question_20 = models.TextField(blank=True, null=True)
    answer_20 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kydata'

class cet4data(models.Model):
    year = models.CharField(max_length=255, blank=True, null=True)
    section_type = models.CharField(max_length=255, blank=True, null=True)
    text_content = models.TextField(blank=True, null=True)
    question_1 = models.TextField(blank=True, null=True)
    answer_1 = models.CharField(max_length=255, blank=True, null=True)
    question_2 = models.TextField(blank=True, null=True)
    answer_2 = models.CharField(max_length=255, blank=True, null=True)
    question_3 = models.TextField(blank=True, null=True)
    answer_3 = models.CharField(max_length=255, blank=True, null=True)
    question_4 = models.TextField(blank=True, null=True)
    answer_4 = models.CharField(max_length=255, blank=True, null=True)
    question_5 = models.TextField(blank=True, null=True)
    answer_5 = models.CharField(max_length=255, blank=True, null=True)
    question_6 = models.TextField(blank=True, null=True)
    answer_6 = models.CharField(max_length=255, blank=True, null=True)
    question_7 = models.TextField(blank=True, null=True)
    answer_7 = models.CharField(max_length=255, blank=True, null=True)
    question_8 = models.TextField(blank=True, null=True)
    answer_8 = models.CharField(max_length=255, blank=True, null=True)
    question_9 = models.TextField(blank=True, null=True)
    answer_9 = models.CharField(max_length=255, blank=True, null=True)
    question_10 = models.TextField(blank=True, null=True)
    answer_10 = models.CharField(max_length=255, blank=True, null=True)
    question_11 = models.TextField(blank=True, null=True)
    answer_11 = models.CharField(max_length=255, blank=True, null=True)
    question_12 = models.TextField(blank=True, null=True)
    answer_12 = models.CharField(max_length=255, blank=True, null=True)
    question_13 = models.TextField(blank=True, null=True)
    answer_13 = models.CharField(max_length=255, blank=True, null=True)
    question_14 = models.TextField(blank=True, null=True)
    answer_14 = models.CharField(max_length=255, blank=True, null=True)
    question_15 = models.TextField(blank=True, null=True)
    answer_15 = models.CharField(max_length=255, blank=True, null=True)
    question_16 = models.TextField(blank=True, null=True)
    answer_16 = models.CharField(max_length=255, blank=True, null=True)
    question_17 = models.TextField(blank=True, null=True)
    answer_17 = models.CharField(max_length=255, blank=True, null=True)
    question_18 = models.TextField(blank=True, null=True)
    answer_18 = models.CharField(max_length=255, blank=True, null=True)
    question_19 = models.TextField(blank=True, null=True)
    answer_19 = models.CharField(max_length=255, blank=True, null=True)
    question_20 = models.TextField(blank=True, null=True)
    answer_20 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cet4data'

class cet6data(models.Model):
    year = models.CharField(max_length=255, blank=True, null=True)
    section_type = models.CharField(max_length=255, blank=True, null=True)
    text_content = models.TextField(blank=True, null=True)
    question_1 = models.TextField(blank=True, null=True)
    answer_1 = models.CharField(max_length=255, blank=True, null=True)
    question_2 = models.TextField(blank=True, null=True)
    answer_2 = models.CharField(max_length=255, blank=True, null=True)
    question_3 = models.TextField(blank=True, null=True)
    answer_3 = models.CharField(max_length=255, blank=True, null=True)
    question_4 = models.TextField(blank=True, null=True)
    answer_4 = models.CharField(max_length=255, blank=True, null=True)
    question_5 = models.TextField(blank=True, null=True)
    answer_5 = models.CharField(max_length=255, blank=True, null=True)
    question_6 = models.TextField(blank=True, null=True)
    answer_6 = models.CharField(max_length=255, blank=True, null=True)
    question_7 = models.TextField(blank=True, null=True)
    answer_7 = models.CharField(max_length=255, blank=True, null=True)
    question_8 = models.TextField(blank=True, null=True)
    answer_8 = models.CharField(max_length=255, blank=True, null=True)
    question_9 = models.TextField(blank=True, null=True)
    answer_9 = models.CharField(max_length=255, blank=True, null=True)
    question_10 = models.TextField(blank=True, null=True)
    answer_10 = models.CharField(max_length=255, blank=True, null=True)
    question_11 = models.TextField(blank=True, null=True)
    answer_11 = models.CharField(max_length=255, blank=True, null=True)
    question_12 = models.TextField(blank=True, null=True)
    answer_12 = models.CharField(max_length=255, blank=True, null=True)
    question_13 = models.TextField(blank=True, null=True)
    answer_13 = models.CharField(max_length=255, blank=True, null=True)
    question_14 = models.TextField(blank=True, null=True)
    answer_14 = models.CharField(max_length=255, blank=True, null=True)
    question_15 = models.TextField(blank=True, null=True)
    answer_15 = models.CharField(max_length=255, blank=True, null=True)
    question_16 = models.TextField(blank=True, null=True)
    answer_16 = models.CharField(max_length=255, blank=True, null=True)
    question_17 = models.TextField(blank=True, null=True)
    answer_17 = models.CharField(max_length=255, blank=True, null=True)
    question_18 = models.TextField(blank=True, null=True)
    answer_18 = models.CharField(max_length=255, blank=True, null=True)
    question_19 = models.TextField(blank=True, null=True)
    answer_19 = models.CharField(max_length=255, blank=True, null=True)
    question_20 = models.TextField(blank=True, null=True)
    answer_20 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cet6data'

class Year(models.Model):
    name = models.CharField(max_length=255)  # 将最大长度修改为255

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'myapp_year'

class Cet4_year(models.Model):
    name = models.CharField(max_length=255)  # 将最大长度修改为255

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'cet4year'

class Cet6_year(models.Model):
    name = models.CharField(max_length=255)  # 将最大长度修改为255

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'cet6year'



class Wordbook(models.Model):
    user = models.ForeignKey(User, related_name='wordbook', on_delete=models.CASCADE)
    word = models.CharField(max_length=100)
    phonetic = models.CharField(max_length=255, blank=True, null=True)
    translation = models.TextField(blank=True, null=True)
    added_at = models.DateTimeField(default=timezone.now)

    def get_audio_url(self):
        first_letter = self.word[0].lower()  # 获取单词首字母并转换为小写
        audio_file = self.word + '.wav'
        # 构建音频文件的路径
        return os.path.join(settings.STATIC_URL, 'fayin', 'Lingoes English', 'voice', first_letter, audio_file)

    class Meta:
        db_table = 'wordbook'
        unique_together = ['user', 'word']

    def __str__(self):
        return self.word


class UserSettingsWordbook(models.Model):
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
        db_table = 'usersettingsWordbook'






