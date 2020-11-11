from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def user_detail(request, pk):
    """
    List all code snippets, or create a new snippet.
    """
    try:
        user = User.objects.get(pk = pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('email')
    serializer_class = UserSerializer

class AwardViewSet(viewsets.ModelViewSet):
    queryset = Award.objects.all().order_by('award_id')
    serializer_class = AwardSerializer

class ContactInfoViewSet (viewsets.ModelViewSet):
    queryset = ContactInfo.objects.all().order_by('contact_id')
    serializer_class = ContactInfoSerializer

class EducationViewSet (viewsets.ModelViewSet):
    queryset = Education.objects.all().order_by('edu_id')
    serializer_class = EducationSerializer

class ExperienceViewSet (viewsets.ModelViewSet):
    queryset = Experience.objects.all().order_by('exp_id')
    serializer_class = ExperienceSerializer

class ProjectViewSet (viewsets.ModelViewSet):
    queryset = Project_Experience.objects.all().order_by('project_id')
    serializer_class = ProjectSerializer

class SkillViewSet (viewsets.ModelViewSet):
    queryset = Skill.objects.all().order_by('skill_id')
    serializer_class = SkillSerializer