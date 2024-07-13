from rest_framework.views import APIView
from rest_framework.response import Response #when call api view return res
from rest_framework import status #list of of handy http  EG. BAD HTTP_400_BAD_REQUEST
from profiles_api import serializers #FILE created in profiles api


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
