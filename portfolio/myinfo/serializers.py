from rest_framework import serializers
from .models import MyInfo, Home, Projects, Contact, Skills, SocialMediaLinks,WorkExperience, ExamCracked, ParticipationCertificate, OtherSkill


class MyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyInfo
        fields = '__all__'

class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = '__all__'


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'

class SocialMediaLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaLinks
        fields = '__all__'
class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = ['id', 'position', 'description', 'certificates']


class ExamCrackedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamCracked
        fields = ['id', 'exam_type', 'description']

class ParticipationCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipationCertificate
        fields = ['id', 'image']

class OtherSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherSkill
        fields = ['id', 'skill']