from rest_framework import generics, filters, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Artist, Work, Client
from .serializers import ArtistSerializer, WorkSerializer, RegistrationSerializer


class WorkList(generics.ListAPIView):
    serializer_class = WorkSerializer
    queryset = Work.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['artist__name','work_type']
    ordering_fields = ['id', 'link', 'work_type']

    def get_queryset(self):
        queryset = super().get_queryset()
        artist_name = self.request.query_params.get('artist', None)
        work_type = self.request.query_params.get('work_type', None)
        if artist_name is not None:
            queryset = queryset.filter(artist__name__icontains=artist_name)
        if work_type:
            queryset = queryset.filter(work_type=work_type)
        return queryset


class RegistrationView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.create_user(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )
        client = Client.objects.create(user=user)
        headers = self.get_success_headers(serializer.data)
        return Response({'user_id': user.id, 'client_id': client.id}, status=201, headers=headers)


class ArtistViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    @action(methods=['get'], detail=True)
    def works(self, request, pk=None):
        artist = self.get_object()
        works = artist.work_set.all()
        serializer = WorkSerializer(works, many=True)
        return Response(serializer.data)


