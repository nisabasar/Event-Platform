from urllib import response
from rest_framework import status
from rest_framework import viewsets, permissions
from .models import User, Event, Participant, Message
from .serializers import UserSerializer, EventSerializer, ParticipantSerializer, MessageSerializer
from datetime import timedelta


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        # Yeni etkinlik bilgilerini al
        event_data = request.data
        user = request.user
        new_event_start = f"{event_data['date']}T{event_data['time']}"
        new_event_duration = timedelta(hours=float(event_data['duration']))
        new_event_end = new_event_start + new_event_duration

        # Kullanıcının mevcut etkinliklerini al
        user_events = Event.objects.filter(created_by=user)

        for event in user_events:
            existing_event_start = f"{event.date}T{event.time}"
            existing_event_duration = timedelta(hours=float(event.duration))
            existing_event_end = existing_event_start + existing_event_duration

            # Zaman çakışması kontrolü
            if new_event_start < existing_event_end and new_event_end > existing_event_start:
                return response({'error': 'Zaman çakışması: Bu etkinlik başka bir etkinliğinizle çakışıyor.'}, status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)

class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = request.user
        event_id = request.data.get('event')
        
        # Etkinlik kontrolü
        if Participant.objects.filter(user=user, event_id=event_id).exists():
            return response({'error': 'Bu etkinliğe zaten katıldınız.'}, status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        event_id = self.request.query_params.get('event')
        if event_id:
            return self.queryset.filter(event_id=event_id)
        return self.queryset
