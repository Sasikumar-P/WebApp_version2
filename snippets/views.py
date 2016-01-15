from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import permissions
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework.renderers import JSONRenderer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework import status
from rest_framework.parsers import JSONParser
from snippets.models import Snippet, Author, Mark, Note, Hard, Soft, Book
from snippets.serializers import SnippetSerializer, AuthorSerializer,MarkSerializer,NoteSerializer,HardSerializer, SoftSerializer, BookSerializer, UserSerializer
def home(request):
	return render(request, 'home.html')
def hello(request):
	return render(request, 'hello.html')

def new(request):
	return render(request, 'new.html')
def note(request):
	return render(request, 'note.html')
def jjj(request):
	return render(request,'hard.html')
def iii(request):
	return render(request,'soft.html')
def kkk(request):
	return render(request,'book.html')



class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
    def perform_create(self, serializer):
    	serializer.save(owner=self.request.user)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

@csrf_exempt
def mark_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        mark = Mark.objects.all()
        serializer = MarkSerializer(mark, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MarkSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def mark_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        mark = Mark.objects.get(pk=pk)
    except Mark.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MarkSerializer(mark)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MarkSerializer(mark, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)
@csrf_exempt
def note_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        note = Note.objects.all()
        serializer = NoteSerializer(note, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Noteerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def note_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        note = Note.objects.get(pk=pk)
    except Note.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = NoteSerializer(mark)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = NoteSerializer(note, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        mark.delete()
        return HttpResponse(status=204)
@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)
@csrf_exempt
def author_detail(request,pk):
	try:
		author = Author.objects.get(pk=pk)
	except Author.DoesNotExists:
		return HttpResponse(status=404)
        if request.method == 'GET':
               serializer = AuthorSerializer(author)
               return JSONResponse(serializer.data)
     
        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = AuthorSerializer(author, data=data)
            if serializer.is_valid():
                 serializer.save()
                 return JSONResponse(serializer.data)
            return JSONResponse(serializer.errors, status=400)

        elif request.method == 'DELETE':
             snippet.delete()
             return HttpResponse(status=204)
@csrf_exempt
def author_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AuthorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
class HardList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        hard = Hard.objects.all()
        serializer = HardSerializer(hard, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = HardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class HardDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Hard.objects.get(pk=pk)
        except Hard.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        hard = self.get_object(pk)
        serializer = HardSerializer(hard)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        hard = self.get_object(pk)
        serializer = HardSerializer(hard, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        hard = self.get_object(pk)
        hard.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SoftList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Soft.objects.all()
    serializer_class = SoftSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class SoftDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Soft.objects.all()
    serializer_class = SoftSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
