import datetime
from dateutil.relativedelta import relativedelta as date_diff
from datetime import date
from django.core.exceptions import ValidationError
from rest_framework import serializers


def check_birth_date(value: date):
    age = date_diff(datetime.date.today(), value).years
    if age < 9:
        raise serializers.ValidationError(f"Минимальный возраст для регистрации - 9, Ваш {age}")


def check_email(value: str):
    if "rambler.ru" in value:
        raise ValidationError("Error registry domens rambler.ru not used")
