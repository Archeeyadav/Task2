from rest_framework import serializers
from .models import CarListing, UserProfile, Product, Contact
from rest_framework.authtoken.models import Token

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["first_name", "last_name", "email", "password", "profile"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = UserProfile(
            username=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
            profile=validated_data["profile"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class CarListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarListing
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()
    total_spent = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = "__all__"
    
    def get_profile(self, obj):
        return obj.user.profile
    
    def get_total_spent(self, obj):
        return obj.clicks * obj.amount_charges
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.clicks >= instance.max_clicks:
            data['button_disable'] = True
        else:
            data['button_disable'] = False
        return data

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"
