from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField('标题',max_length=50)
    category = models.CharField('分类',max_length=50, blank=True)
    publish_time = models.DateField('发布时间',auto_now_add=True)
    content = models.TextField('正文')
    # modify_date = models.DateField('修改日期',auto_now=True)
    # author = models.CharField('作者',max_length=50)

    class Meta:
        db_table = 'article'  #数据库表名
        ordering = ['-publish_time']  # 按发布日期倒序排列

    def __str__(self):
        return self.title
