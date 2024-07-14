from rest_framework.views import APIView
from rest_framework.response import Response #when call api view return res
from rest_framework import status #list of of handy http  EG. BAD HTTP_400_BAD_REQUEST
from profiles_api import serializers,models #FILE created in profiles api
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
# Create your views here.

#How it works
#define url which is endpoint then assign it to
#views then django returns correct res
class HelloApiView(APIView):#class based on APIView
    """test api view"""
    serializer_class = serializers.HelloSerializer #ACCESSED OUR SERIALIZER class

    #accept get request
    def get(self, request, format=None):
        """return a list of apiview features"""
        an_apiview = [
        'uses http methods as funtions(get,post,put,delete,patch)',
        'apiview is similar to ordinary django',
        'gives you the ost control over app logic',
        'is mapped manually',
        'my name is tonny ',
        ]

        return Response({'our_message':'Hello ', 'an_apiview':an_apiview})#contain a dictionary or list convert res to json = list or dict

    def post(self, request):
        """post method to return hello with passed name that is serialized"""
        serializer = self.serializer_class(data=request.data)#PASSED ARGUMENTS OF HelloSerializer CLASS - CHECKS ALL VALIDATES RULESS IN THE SERIALIZER CLASS

        if serializer.is_valid():
            returned_name = serializer.validated_data.get('name')
            returned_username = serializer.validated_data.get('username')
            message = f'Welcome to programming {returned_name}'
            message2 = f'validated username {returned_username}'
            return Response({ 'our_message':message,'our_message2':message2 })
        else:
            return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )
    def put(self, request, pk=None):
        """hanle updating an object - REPLACING"""
        return Response({ 'method':'PUT' })

    def patch(self, request, pk=None):
        """handle partial update UPDATING"""
        return Response({ 'method':'PATCH' })

    def delete(self, request,pk=None):
        """delete an object permanentky"""
        return Response({ 'method':'DELETE' })

class HelloViewSet(viewsets.ViewSet):
    """test api ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """return hello message with list"""

        a_viewset = [
            'uses actions (list,create,retrieve,update,partial_update)',
            'Automaticallly maps urls using routers',
            'more functionality with les code',
        ]
        return Response({ 'message':'Hello', 'a_viewset':a_viewset })


    def create(self, request):
        """create a new hwllo message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            returned_name = serializer.validated_data.get('name')
            returned_username = serializer.validated_data.get('username')
            message = f'Welcome {returned_name} and {returned_username}'
            return Response({ 'message':message })
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


    def retrieve(self, request, pk=None):
        """getting object by ID"""
        return Response({ 'http_method':'GET' })


    def update(self, request, pk=None):
        """handle update an object"""
        return Response({ 'http_method':'PUT' })


    def partial_update(self, request, pk=None):
        """handle partial_update of object"""
        return Response({ 'http_method':'PATCH' })


    def destroy(self, request, pk=None):
        """handle removing object"""
        return Response({ 'http_method':'DELETE' })



class UserProfileViewSet(viewsets.ModelViewSet):
    """handel create and update profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """handle create user auth"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """create,read and update profilefeeditem"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticated,
    )#user ust be authenticated to perform any changes


    def perform_create(self, serializer):#handy feature to customize criteria of creating
        """only set user profile for the logged in user"""
        serializer.save(user_profile=self.request.user)
