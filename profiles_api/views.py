from rest_framework.views import APIView
from rest_framework.response import Response #when call api view return res


# Create your views here.
#How it works
#define url which is endpoint then assign it to
#views then django returns correct res
class HelloApiView(APIView):#class based on APIView
    """test api view"""
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
