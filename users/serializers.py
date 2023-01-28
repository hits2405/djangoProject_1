from django.db.models import Count
from rest_framework import serializers

from users.models import User, Location


class UserLS(serializers.ModelSerializer):
    total_ad = serializers.IntegerField()
    locations = serializers.SlugRelatedField(many=True, queryset=Location.objects.all(), slug_field='name')

    class Meta:
        model = User
        exclude = ['password']


class UserDS(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(many=True, slug_field='name', queryset=Location.objects.all())

    class Meta:
        model = User
        exclude = ['password']
        # fields = '__all__'


class UserCS(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(required=False, many=True, slug_field='name',
                                             queryset=Location.objects.all())

    def is_valid(self, *, raise_exception=False):
        self._locations = self.initial_data.pop('locations', [])
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        pas = validated_data.pop("password")
        new_user = User.objects.create(**validated_data)
        new_user.set_password(pas)
        new_user.save()

        for locate in self._locations:
            location, _ = Location.objects.get_or_create(name=locate)
            new_user.locations.add(location)
        return new_user

    class Meta:
        model = User
        fields = "__all__"
        #exclude = ['password']


class UserUS(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(required=False, many=True, slug_field='name',
                                             queryset=Location.objects.all())

    def is_valid(self, *, raise_exception=False):
        self._locations = self.initial_data.pop('locations', [])
        return super().is_valid(raise_exception=raise_exception)

    def save(self, **kwargs):
        user = super().save(**kwargs)
        for loc in self._locations:
            location, _ = Location.objects.get_or_create(name=loc)
            user.locations.add(location)
        return user

    class Meta:
        model = User
        exclude = ['password']


class LocationMS(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
