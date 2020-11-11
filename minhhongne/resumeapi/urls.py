from django.urls import include, path, re_path
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register(r'users', views.UserViewSet)
router.register(r'awards', views.AwardViewSet)
router.register(r'contactInfo', views.ContactInfoViewSet)
router.register(r'educations', views.EducationViewSet)
router.register(r'experiences', views.ExperienceViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'skills', views.SkillViewSet)

urlpatterns= [
    path('', include(router.urls)),
    re_path('users/<int:pk>', views.user_detail),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
# urlpatterns = router.urls