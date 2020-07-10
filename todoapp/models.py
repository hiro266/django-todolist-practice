from django.db import models

# (('保存される文字列','ビューに表示される文字列'))
PRIORITY = (('danger','high'),('info','normal'),('success','low'))

# モデルの作成 引数にはmodels.Modelモジュールを継承
class TodoModel(models.Model):
    # models.CharFiels = 文字列のフィールド 引数必須
    # models.TextField = 長い文字列
    title = models.CharField(max_length = 100)
    memo = models.TextField()
    priority = models.CharField(
      max_length=50,
      # choices = selectボックスのようにできる
      choices = PRIORITY
    )
    duedate = models.DateField()
    # オブジェクトを文字列として返す
    # self = classから出来上がった一つ一つのオブジェクト
    def __str__(self):
        return self.title
