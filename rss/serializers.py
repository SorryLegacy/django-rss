from .models import PostFromUrl
from rest_framework import serializers


class PostSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PostFromUrl
        fields = ['title', 'date', 'link', 'img']
