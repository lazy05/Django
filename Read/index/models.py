from django.db import models

# Create your models here.
class UserInfo(models.Model):
    uname = models.CharField('用户名',max_length=50,null=False)
    upassword = models.CharField('密码',max_length=200,null=False)
    email = models.CharField('邮箱',max_length=50,null=True)
    time = models.DateTimeField('注册时间',auto_now_add=True)
    isban = models.BooleanField('禁用',default=False)
    isdelete = models.BooleanField('删除',default=False)

    def __str__(self):
        return self.uname

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class content(models.Model):
    name = models.CharField('名称',max_length=500,null=False)
    content = models.CharField('内容',max_length=1024000,null=False)
    li = models.CharField('编号',max_length=100,null=False)
    time = models.DateTimeField('上传时间',auto_now_add=True)
    isdelete = models.BooleanField('删除',default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '文章名称'
        verbose_name_plural = verbose_name

class Commit(models.Model):
    matter = models.CharField('评论内容',max_length=10000)
    time = models.DateTimeField('评论时间',auto_now_add=True)
    title = models.ForeignKey(content)
    user = models.ForeignKey(UserInfo)

    def __str__(self):
        return self.matter

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
