from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BlogSerializer, BlogReadSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOrReadOnly
from .models import Blog
import datetime
from django.db import connection

class BlogView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            blog = Blog.objects.get(id=pk)
            
            return Response({
                    'data': BlogReadSerializer(instance=blog).data
                }, status = status.HTTP_200_OK)
        
        except Blog.DoesNotExist:
            return Response({
                'data': {},
                'message': "Blog doesn't exist",
            }, status = status.HTTP_400_BAD_REQUEST)
        

    def post(self, request):
        try:
            data = request.data
            data['author'] = request.user.id
            serializer = BlogSerializer(data=data)
            
            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message': 'something went wrong!'
                }, status = status.HTTP_400_BAD_REQUEST)
            serializer.save()

            return Response({
                'data': serializer.data,
                'message': 'blog created successfully!'   
            }, status = status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response({
                'data': {},
                'message': 'something went wrong!'
            }, status = status.HTTP_400_BAD_REQUEST)
        

    def patch(self, request):
        try:
            data = request.data

            # blog = Blog.objects.filter(uid =data.get('uid'))
            blog = Blog.objects.get(id=data.get('id'))

            if request.user != blog.author:
                return Response({
                'data': {},
                'message': 'you are not authorized to this'
            }, status = status.HTTP_400_BAD_REQUEST)

            serializer = BlogSerializer(blog, data=data, partial=True)
             
            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message': 'something went wrong!'
                }, status = status.HTTP_400_BAD_REQUEST)
            
            serializer.save()

            return Response({
                'data': serializer.data,
                'message': 'blog updated successfully!'   
            }, status = status.HTTP_200_OK)
        
        except Exception as e:
            print(e)
            return Response({
                'data': {},
                'message': 'something went wrong!'
            }, status = status.HTTP_400_BAD_REQUEST)
        

    def delete(self, request, pk):
        try:
            blog = Blog.objects.get(id=pk)

            if request.user != blog.author:
                return Response({
                'data': {},
                'message': 'you are not authorized to this'
            }, status = status.HTTP_400_BAD_REQUEST)

            blog.delete()
            return Response({
                'message': 'Blog has been deleted!'
            },status=status.HTTP_204_NO_CONTENT)
        
        except Blog.DoesNotExist:
            return Response({
                'data': {},
                'message': "Blog doesn't exist",
            }, status = status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            print(e)
            return Response({
                'data': {},
                'message': 'something went wrong!'
            }, status = status.HTTP_400_BAD_REQUEST)
        
        

class BlogsView(APIView):
    
    def get(self, request):
        
        title = request.query_params.get('title')
        author_name = request.query_params.get('author_name')
        publication_date = request.query_params.get('publication_date')
        
        title = None if not title else title
        author_name = None if not author_name else author_name
        publication_date = None if not publication_date else publication_date

        try:
            if publication_date is not None:
                datetime.date.fromisoformat(publication_date)
        except ValueError:
            return Response({
                'data': {},
                'message': 'Date must be in ISO format!'
            }, status = status.HTTP_400_BAD_REQUEST)


        title = ('"'+title+'"') if title else 'null'
        author_name = ('"'+author_name+'"') if author_name else 'null'
        publication_date = ('"'+publication_date+'"') if publication_date else 'null'
        
        sp_call_query = f'''
            call sp_getBlogs({title}, {author_name}, {publication_date})
        '''

        cursor = connection.cursor()
        cursor.execute(sp_call_query)
        results = []
        columns = [column[0] for column in cursor.description]
        for row in cursor.fetchall():
            results.append(dict(zip(columns, row)))


        return Response({
                'data': results,
                'message': 'success!'   
            }, status = status.HTTP_200_OK)

