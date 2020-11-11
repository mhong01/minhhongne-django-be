from rest_framework import serializers
from resumeapi.models import *

class UserSerializer (serializers.HyperlinkedModelSerializer):
    # awards = serializers.StringRelatedField(many=True)
    # info = serializers.StringRelatedField(many=True)
    # educations = serializers.StringRelatedField(many=True)
    # experiences = serializers.StringRelatedField(many=True)
    # skills = serializers.StringRelatedField(many=True)
    class Meta:
        model = User
        fields = ('id', 'email', 'firstName', 'lastName',
                  'info', 'awards', 'educations',
                  'experiences','skills')

class AwardSerializer( serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Award
        fields = ('award_id', 'event', 'award_name', 'award_year', 'description')

class ContactInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContactInfo
        fields = ('contact_id', 'address', 'tel', 'email', 'linkedin', 'github')

class EducationSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Education
        fields = ('edu_id', 'school_name', 'location', 'program', 'duration')

class ExperienceSerializer (serializers.HyperlinkedModelSerializer):
    projects = serializers.StringRelatedField(many=True)
    class Meta:
        model = Experience
        fields = ('exp_id', 'projects', 'role', 'company', 'location', 'duration', 'website', 'overview')

class ProjectSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project_Experience
        fields = ('project_id', 'name', 'overview', 'duties')

class SkillSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Skill
        fields = ('skill_id', 'skill_name', 'description')