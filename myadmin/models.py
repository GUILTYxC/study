from django.db import models
from datetime import datetime, timedelta
from django.utils import timezone
from django.db.models import F  # 导入 F
import pytz





#用户账号信息模型
class User(models.Model):
    username = models.CharField(max_length=50)    # 员工账号
    nickname = models.CharField(max_length=50)    # 昵称
    password_hash = models.CharField(max_length=100)  # 密码
    password_salt = models.CharField(max_length=50)   # 密码干扰值
    status = models.IntegerField(default=1)       # 状态: 1正常 / 2禁用 / 9删除
    create_at = models.DateTimeField(default=timezone.now)  # 创建时间
    update_at = models.DateTimeField(default=timezone.now)  # 修改时间

    def is_activated(self):
        # 检查是否存在至少一个已激活且未过期的卡
        return self.cards.filter(is_activated=True, activated_at__lte=timezone.now(),
                                 activated_at__gte=timezone.now() - timedelta(days=F('duration'))).exists()

    def toDict(self):
        return {
            'id': self.id,
            'username': self.username,
            'nickname': self.nickname,
            'password_hash': self.password_hash,
            'password_salt': self.password_salt,
            'status': self.status,
            'create_at': self.create_at.strftime('%Y-%m-%d %H:%M:%S'),
            'update_at': self.update_at.strftime('%Y-%m-%d %H:%M:%S')
        }

    class Meta:
        db_table = "user"  # 更改表名



class Card(models.Model):
    code = models.CharField(max_length=20, unique=True)  # 卡密
    duration = models.IntegerField()  # 有效期（天）
    is_activated = models.BooleanField(default=False)  # 是否已激活
    ai_activated = models.BooleanField(default=False)  # AI功能是否激活
    activated_at = models.DateTimeField(null=True, blank=True)  # 激活时间
    create_at = models.DateTimeField(default=timezone.now)  # 创建时间
    update_at = models.DateTimeField(default=timezone.now)  # 修改时间
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='cards')  # 关联的用户
    remark = models.TextField(blank=True, null=True)  # 备注

    def is_expired(self):
        if self.is_activated and self.activated_at:
            expiration_date = self.activated_at + timedelta(days=self.duration)
            return expiration_date < timezone.now()
        return False

    def save(self, *args, **kwargs):
        if not self.id:  # 新建记录
            self.create_at = timezone.now()
        self.update_at = timezone.now()  # 更新时间
        super().save(*args, **kwargs)

    def __str__(self):
        return self.code

    class Meta:
        db_table = "card"  # 更改表名







