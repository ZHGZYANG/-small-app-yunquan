# _*_ coding:utf-8 _*_
from django.db import models
from datetime import datetime
from user_info.models import UserMessage
# Create your models here.


class Moments(models.Model):
    moments_user = models.ForeignKey(UserMessage,verbose_name=u'用户')
    moments_text = models.TextField(verbose_name=u'说说正文')
    moments_img = models.ImageField(upload_to='image/%Y/%m', default=u'image/default.png', max_length=100,verbose_name=u"图片信息")
    moments_like = models.IntegerField(default=0,verbose_name=u'点赞数')
    moments_comment = models.TextField(null=True,verbose_name=u'评论')
    has_delete = models.BooleanField(default=False, verbose_name=u"是否已删除")
    moments_add_time = models.DateTimeField(default=datetime.now, verbose_name=u"说说添加时间")
    user_friends_id = models.TextField(null=True, verbose_name=u"用户好友ID")

    class Meta:
        verbose_name = u"用户说说信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}({1})'.format(self.id, self.moments_user)
