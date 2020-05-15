from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator
from rest_framework.relations import HyperlinkedIdentityField

User = get_user_model()

class UserCreateSerialiazer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        label='Email',
        validators=[UniqueValidator(queryset=User.objects.all())])

    password = serializers.CharField(label='Password', min_length=8, write_only=True, 
                                     style={'input_type': 'password', 'placeholder': 'Password'})
    password2 = serializers.CharField(label='Confirm Password', write_only=True, 
                                      style={'input_type': 'password', 'placeholder': 'Password'})

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name',
                  'password', 'password2',)

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        user = User(username=username, 
                    email=email, 
                    first_name=first_name, 
                    last_name=last_name,)
                
        if password != validated_data['password2']:
            raise ValidationError('Passwords not match!')
        else:
            user.set_password(password)
            user.save()
        return validated_data



class UserSerializer(serializers.HyperlinkedModelSerializer):
   
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'first_name', 'last_name',
                  'email')


