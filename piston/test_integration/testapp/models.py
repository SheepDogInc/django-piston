from django.db import models

class TestModel(models.Model):
    test1 = models.CharField(max_length=1, blank=True, null=True)
    test2 = models.CharField(max_length=1, blank=True, null=True)
    
class ExpressiveTestModel(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    never_shown = models.TextField()

class IntegerTestModel(models.Model):
    name = models.CharField(max_length=255)
    offices_count = models.IntegerField(blank=True, null=True)

class Comment(models.Model):
    parent = models.ForeignKey(ExpressiveTestModel, related_name='comments')
    content = models.TextField()

class AbstractModel(models.Model):
    some_field = models.CharField(max_length=32, default='something here')
    
    class Meta:
        abstract = True
        
class InheritedModel(AbstractModel):
    some_other = models.CharField(max_length=32, default='something else')
    
    class Meta:
        db_table = 'testing_abstracts'

class PlainOldObject(object):
    def __emittable__(self):
        return {'type': 'plain',
                'field': 'a field'}

class ListFieldsModel(models.Model):
    kind = models.CharField(max_length=15)
    variety = models.CharField(max_length=15)
    color = models.CharField(max_length=15)

class Issue58Model(models.Model):
    read = models.BooleanField(default=False)
    model = models.CharField(max_length=1, blank=True, null=True)
