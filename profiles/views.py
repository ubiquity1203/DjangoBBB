# Create your views here.
from django.http.response import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from profiles.models import Profile
from profiles.serializers import ProfileSerializer


class ProfileApiView(APIView):
    """
    Retrieve a profile instance.
    """
    def get_object(self, user):
        try:
            return Profile.objects.get(user=user)
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        user = request.user
        profile = self.get_object(user)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request, format=None):
        user = request.user
        return