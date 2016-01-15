from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    

    class Meta:
        ordering = ('created',)


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()



class Mark(models.Model):
	malayalam = models.IntegerField(default=0)
        physics = models.IntegerField(default=0)
	chemistry = models.IntegerField(default=0)
	maths = models.IntegerField(default=0)

class Note(models.Model):
	page1 = models.IntegerField(default=0)
        page2 = models.IntegerField(default=0)
	page3 = models.IntegerField(default=0)
	page4 = models.IntegerField(default=0)
class Hard(models.Model):
	rigid = models.IntegerField(default=0)
        soft = models.IntegerField(default=0)

class Soft(models.Model):
	application = models.IntegerField(default=0)
        system = models.IntegerField(default=0)
class Book(models.Model):
	name = models.IntegerField(default=0)
        author = models.IntegerField(default=0)
