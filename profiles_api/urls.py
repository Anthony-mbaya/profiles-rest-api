from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views


router = DefaultRouter() #router creates all the 4 urls
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset') #resgister specific viewset
router.register('profile',views.UserProfileViewSet)
router.register('feed',views.UserProfileFeedViewSet)

urlpatterns = [
    path('hello/', views.HelloApiView.as_view()),
    path('login/',views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]
