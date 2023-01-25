from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from eds.models import Ad, Category
from users.models import Location, User


class AdDetailS(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', queryset=User.objects.all())
    category = SlugRelatedField(slug_field='name', queryset=Category.objects.all())

    class Meta:
        model = Ad
        fields = '__all__'


class AdLS(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field="id", queryset=User.objects.all())
    category = SlugRelatedField(slug_field="id", queryset=Category.objects.all())
    locations = serializers.SerializerMethodField()

    def get_locations(self, ad):
        return [loc.name for loc in ad.author.locations.all()]

    class Meta:
        model = Ad
        fields = '__all__'


class AdCS(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(required=False, many=True, slug_field='name',
                                             queryset=Location.objects.all())

    def is_valid(self, *, raise_exception=False):
        self._locations = self.initial_data.pop('locations', [])
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        eds = Ad.objects.create(**validated_data)
        for locate in self._locations:
            location, _ = Location.objects.get_or_create(name=locate)
            eds.locations.add(location)
        eds.save()
        return eds

    class Meta:
        model = Ad
        fields = ["id", "name", "author", "price", "locations"]


class AdUS(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(required=False, many=True, slug_field='name',
                                             queryset=Location.objects.all())

    created = serializers.DateField(read_only=True)

    def is_valid(self, *, raise_exception=False):
        self._locations = self.initial_data.pop('locations', [])
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        ad = super().save()
        for loc in self._locations:
            location, _ = Location.objects.get_or_create(name=loc)
            ad.locations.add(location)
        ad.save()
        return ad

    class Meta:
        model = Ad
        fields = ["id", "name", "author", "price", "locations", "created"]


class AdDeleteS(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ["id"]