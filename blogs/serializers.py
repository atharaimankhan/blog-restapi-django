from rest_framework.serializers import (
    ModelSerializer,
    ListField,
    CharField,
    )


from authors.serializers import CustomUserSerializer
from .models import Blog


class TagsSerializerField(ListField):
    child = CharField()
    
    def to_representation(self, data):
        return data.values_list('name', flat=True)
    

class BlogSerializer(ModelSerializer):
    tags = TagsSerializerField(required=False)
    class Meta:
        model = Blog
        exclude = ['published_at']
        

class BlogReadSerializer(ModelSerializer):
    tags = TagsSerializerField(required=False)
    author_firstname = CharField(source='author.first_name')
    author_lastname = CharField(source='author.last_name')
    author_email = CharField(source='author.email')

    class Meta:
        model = Blog
        fields = '__all__'