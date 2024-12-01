from rest_framework import serializers
from .models import User, Event, Participant, Message

from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    gender = serializers.ChoiceField(choices=["male", "female", "other"])
    interests = serializers.ListField(
        child=serializers.CharField(max_length=100), required=False
    )

    class Meta:
        model = User
<<<<<<< HEAD
        fields = ["username", "email", "phone", "password", "gender", "interests"]
=======
        fields = ['username', 'email', 'password', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        return user

>>>>>>> 30d1ff7c2df82ee6731d64731eca4ca5286d5f72

class EventSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    class Meta:
        model = Event
        fields = '__all__'

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
