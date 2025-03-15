from datetime import datetime
from rest_framework import serializers
from .models import Book, Author


class BookSerializer(serializers.ModelSerializer):
    '''
    Serializer Book model here
    '''
    class Meta:
        model = Book
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    '''
    Serializer Author model here and also a validation added for not the user added future dates.
    '''
    book = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name']

    def validate(self, data):
        # Dates should not be future date.
        if data['publication_year'] > datetime.now():
            raise serializers.ValidationError("Date cannot be future.")
        return data