#coding:utf8
from django.db import models

# Create your models here.


#导航菜单
class NavigationMenu(models.Model):
    name = models.CharField(max_length=30, verbose_name='菜单名称')
    index = models.IntegerField(default=999, verbose_name='排序')
    url = models.CharField(max_length=30, verbose_name='Url')

    class Meta:
        verbose_name = '菜单'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __unicode__(self):
        return self.name


# 分类
class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='分类名称')
    title = models.CharField(max_length=64, verbose_name='标题')
    keywords = models.CharField(max_length=255, verbose_name='关键词')

    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name
        ordering = ['-created_time']

    def __unicode__(self):
        return self.name

# tag（标签）
class Tag(models.Model):
    name = models.CharField(max_length=30, verbose_name='标签名称')
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


# 文章模型
class Article(models.Model):
    STATUS_CHOICES = (
        ('0', '发布'),
        ('1', '草稿'),
    )

    title = models.CharField(max_length=50, verbose_name='文章标题')
    abstract = models.CharField(max_length=50, verbose_name='文章摘要')
    content = models.TextField(verbose_name='文章内容')
    click_count = models.IntegerField(default=0, verbose_name='点击次数')
    status = models.CharField(default='0', max_length=1, choices=STATUS_CHOICES, verbose_name='文章状态')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)
    category = models.ForeignKey(Category, blank=True, null=True, verbose_name='分类')
    tag = models.ManyToManyField(Tag, verbose_name='标签')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']

    def __str__(self):
        return self.title


#友情链接
class Links(models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name='友情链接名字')
    url = models.URLField(unique=True, verbose_name='URL')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加日期')

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __unicode__(self):
        return self.name