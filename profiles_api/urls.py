from django.conf.urls import url
from django.conf.urls import include

from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()



router.register('profile',views.UserProfileViewSet)
router.register('country',views.CountryViewSet)
router.register('login',views.LoginViewSet,basename='login')
router.register('feed',views.UserProfileFeedViewSet)

urlpatterns = [
    url('',include(router.urls))
]

