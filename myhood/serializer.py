from rest_framework import serializers
from .models import Neighbourhood,Profile,Business,Post, User
from django.contrib.auth.hashers import make_password
from rest_framework import viewsets



class BusinessSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    neighbourhood = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model =  Business
        fields = ['businessName', 'user', 'photo','neighbourhood', 'businessEmail'] 

class HoodSerializer(serializers.ModelSerializer):
    business_set = BusinessSerializer(many=True)
    class Meta:
        model =  Neighbourhood
        fields = ['id', 'hoodName','photo','hoodLocation', 'occupants_count', 'business_set']   


class UserSerializer(serializers.ModelSerializer):
    neighbourhood = serializers.PrimaryKeyRelatedField(queryset=Neighbourhood.objects.all())
    class Meta:
        model = User
        fields = ['username', 'email', 'is_staff', 'password', 'neighbourhood']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)


class UserRegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    password = serializers.CharField()
    confirm_password = serializers.CharField()
    
    def validate_email(self, email):
        existing = User.objects.filter(email=email).first()
        if existing:
            raise serializers.ValidationError("Someone with that email "
                "address has already registered. Was it you?")
        return email
    def validate(self, data):
        if not data.get('password') or not data.get('confirm_password'):
            raise serializers.ValidationError("Please enter a password and "
                "confirm it.")
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError("Those passwords don't match.")
        return data


class PostSerializer(serializers.ModelSerializer):
    photo = serializers.FileField(required=False)
    # neighbourhood = Neighbourhood.objects.filter(neighbourhood=<Neighbourhood.id)
    class Meta:
        model =  Post
        fields = ['title', 'text', 'user','photo','date','neighbourhood'] 


class ProfileSerializer(serializers.ModelSerializer):
    neighbourhood = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Profile
        fields = ['name', 'idNo', 'neighbourhood', 'status', 'photo', 'user']    

        
