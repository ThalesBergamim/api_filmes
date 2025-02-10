from rest_framework import serializers
from movies.models import Movie
from django.db.models import Avg
from actors.serializers import ActorSerializer
from genres.serializers import GenreSerializer


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

    def validate_released_date(self, value):

        if value.year < 1990:
            raise serializers.ValidationError('A data de lançamento não pode ser anterior a 1990.')
        return value

    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError('Resumo não deve ser maior do que 200 caracteres.')
        return value


class MovieListDetailSerializer (serializers.Serializer):
    rate = serializers.SerializerMethodField(read_only=True)
    actors = ActorSerializer(many=True)
    genre = GenreSerializer()

    class Meta:
        model = Movie
        fields = ['id', 'title', 'released_date', 'rate', 'actors', 'genre', 'resume']

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)

        return None
