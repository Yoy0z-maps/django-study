from rest_framework import viewsets,permissions,generics,status, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from models import Book
from serializers import BookSerializer

@api_view(['GET'])
def HelloAPI(request):
    return Response('Hello, World!')

@api_view(['GET','POST'])
def BooksAPI(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def bookAPI(request, bid):
    book = get_object_or_404(Book, bid=bid)
    serializer = BookSerializer(book)
    return Response(serializer.data, status=status.HTTP_200_OK)