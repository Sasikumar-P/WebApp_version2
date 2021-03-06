from django.forms import widgets
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES,Author, Mark, Note, Hard, Soft, Book
from django.contrib.auth.models import User


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style','owner')

    
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
	model = Author
        fields = ('id','first_name','last_name','email')

class MarkSerializer(serializers.ModelSerializer):
    class Meta:
	model = Mark
        fields = ('id','malayalam','physics','chemistry','maths')

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
	model = Note
        fields = ('id','page1','page2','page3','page4')
class HardSerializer(serializers.ModelSerializer):
    class Meta:
	model = Hard
        fields = ('id','rigid','soft')

class SoftSerializer(serializers.ModelSerializer):
    class Meta:
	model = Soft
        fields = ('id','application','system')
class BookSerializer(serializers.ModelSerializer):
    class Meta:
	model = Book
        fields = ('id','name','author')
class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')
