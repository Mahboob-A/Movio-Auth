# Django
from django.core.validators import MinLengthValidator, MaxLengthValidator

# DRF
from rest_framework import serializers

# JWT
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# Local
from core_apps.users.models import CustomUser


class UserRegistrationAPISerializer(serializers.ModelSerializer):
    """Serializer for registering an User"""

    password = serializers.CharField(
        validators=[
            MinLengthValidator(6, "Password must be at least 6 characters"),
            MaxLengthValidator(16, "Password must be within 16 characters"),
        ],
        style={"input_type": "password"},
        write_only=True,
        required=True,
    )

    password2 = serializers.CharField(
        validators=[
            MinLengthValidator(6, "Password must be at least 6 characters"),
            MaxLengthValidator(16, "Password must be within 16 characters"),
        ],
        style={"input_type": "password"},
        write_only=True,
        required=True,
    )

    class Meta:
        model = CustomUser
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
            "password2",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, attrs):
        pass1 = attrs.get("password")
        pass2 = attrs.get("password2")

        if pass1 and pass2 and pass1 != pass2:
            raise serializers.ValidationError("Password does not match!")
        attrs.pop("password2")
        return attrs

    def create(self, validated_data):
        first_name = validated_data.pop("first_name")
        last_name = validated_data.pop("last_name")
        email = validated_data.pop("email")
        password = validated_data.pop("password")

        return CustomUser.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            **validated_data,
        )


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Serializer class to include some other user info in the jwt claim."""

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # additional user details to the token payload
        token["first_name"] = user.first_name
        token["last_name"] = user.last_name
        token["username"] = user.username
        token["email"] = user.email
        return token
