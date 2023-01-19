from rest_framework import serializers

from users.models import User


class UserDS(serializers.ModelSerializer):
    class Meta:
        model = User
