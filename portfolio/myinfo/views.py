from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MyInfo, Home, Projects, Contact, Skills, SocialMediaLinks, WorkExperience, ExamCracked, ParticipationCertificate, OtherSkill
from .serializers import MyInfoSerializer, HomeSerializer, ProjectsSerializer, ContactSerializer, SkillsSerializer, SocialMediaLinksSerializer,WorkExperienceSerializer, ExamCrackedSerializer, ParticipationCertificateSerializer, OtherSkillSerializer

@api_view(['GET'])
def MyInfo_view(request):
    myinfo_data = MyInfo.objects.first()
    serializer = MyInfoSerializer(myinfo_data)
    return Response(serializer.data)

@api_view(['GET'])
def home_view(request):
    home_data = Home.objects.first()
    serializer = HomeSerializer(home_data)
    return Response(serializer.data)



@api_view(['GET'])
def projects_view(request):
    projects_data = Projects.objects.all()
    serializer = ProjectsSerializer(projects_data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def contact_view(request):
    contact_data = Contact.objects.first()
    serializer = ContactSerializer(contact_data)
    return Response(serializer.data)

@api_view(['GET'])
def skills_view(request):
    skills_data = Skills.objects.all()
    serializer = SkillsSerializer(skills_data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def social_media_links_view(request):
    social_media_links_data = SocialMediaLinks.objects.all()
    serializer = SocialMediaLinksSerializer(social_media_links_data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def work_experience_list(request):
    work_experiences = WorkExperience.objects.all()
    serializer = WorkExperienceSerializer(work_experiences, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def my_info_list(request):
    my_info = MyInfo.objects.all()
    serializer = MyInfoSerializer(my_info, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def exam_cracked_list(request):
    exams_cracked = ExamCracked.objects.all()
    serializer = ExamCrackedSerializer(exams_cracked, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def participation_certificate_list(request):
    participation_certificates = ParticipationCertificate.objects.all()
    serializer = ParticipationCertificateSerializer(participation_certificates, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def other_skill_list(request):
    other_skills = OtherSkill.objects.all()
    serializer = OtherSkillSerializer(other_skills, many=True)
    return Response(serializer.data)