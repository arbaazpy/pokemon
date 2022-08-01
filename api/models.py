from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Boss(BaseModel):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class UserBoss(BaseModel):
    user = models.ForeignKey(User, related_name="bosses", on_delete=models.CASCADE)
    boss = models.ForeignKey(Boss, related_name="bosses", null=True, blank=True, on_delete=models.CASCADE)
    is_ready = models.BooleanField(default=False)
    is_battled = models.BooleanField(default=False)
    battle_date = models.DateTimeField(null=True, blank=True)
    win_streak = models.SmallIntegerField(null=True, blank=True)

    def __str__(self):
        return self.user.username
