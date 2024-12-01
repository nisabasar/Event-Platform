from rest_framework import viewsets, permissions
from .models import User, Event, Participant, Message
from .serializers import UserSerializer, EventSerializer, ParticipantSerializer, MessageSerializer
<<<<<<< HEAD

from rest_framework.response import Response
from rest_framework import status

def update_points(user, action):
    if action == "join":
        user.points += 10
    elif action == "create":
        user.points += 15
    user.save()
=======
from datetime import timedelta
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'create':  # Kayıt işlemi
            return [AllowAny()]
        return [IsAuthenticated()]  # Diğer işlemler için yetkilendirme
>>>>>>> 30d1ff7c2df82ee6731d64731eca4ca5286d5f72

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def create(self, request, *args, **kwargs):
        # Yeni etkinlik verilerini al
        data = request.data
        user = request.user

        # Yeni etkinlik objesini oluştur
        new_event = Event(
            name=data['name'],
            description=data['description'],
            date=data['date'],
            time=data['time'],
            duration=data['duration'],
            location=data['location'],
            category=data['category'],
            created_by=user
        )

        # Zaman çakışması kontrolü
        if check_time_conflict(user, new_event):
            return Response(
                {"detail": "Bu etkinlik, zaman açısından başka bir etkinlikle çakışıyor."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Çakışma yoksa etkinliği kaydet
        new_event.save()
        serializer = self.get_serializer(new_event)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer

    def create(self, request, *args, **kwargs):
        user = request.user
        event_id = request.data.get('event')
        event = Event.objects.get(id=event_id)

        # Zaman çakışması kontrolü
        if check_time_conflict(user, event):
            return Response(
                {"detail": "Bu etkinliğe katılamazsınız, zaman açısından başka bir etkinlikle çakışıyor."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Çakışma yoksa katılımı kaydet
        participant = Participant(user=user, event=event)
        participant.save()
        serializer = self.get_serializer(participant)
        update_points(request.user, "join")
        update_points(request.user, "create")
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

def check_time_conflict(user, new_event):
    # Kullanıcının katıldığı etkinlikleri al
    user_events = Participant.objects.filter(user=user).select_related('event')
    for participant in user_events:
        existing_event = participant.event
        # Tarihler aynı ve zaman çakışıyor mu?
        if new_event.date == existing_event.date and (
            new_event.time < (existing_event.time + existing_event.duration) and
            (new_event.time + new_event.duration) > existing_event.time
        ):
            return True
    return False
from rest_framework import viewsets
from .models import User, Event, Participant, Message
from .serializers import UserSerializer, EventSerializer, ParticipantSerializer, MessageSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer

from rest_framework.permissions import AllowAny

import logging

logger = logging.getLogger(__name__)

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        logger.info(f"Received data: {request.data}")
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
