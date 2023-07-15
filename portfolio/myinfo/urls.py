from django.urls import path
from . import views

urlpatterns = [
    path('Myinfo/', views.MyInfo_view, name='Myinfo'),
    path('home/', views.home_view, name='home'),
    path('projects/', views.projects_view, name='projects'),
    path('contact/', views.contact_view, name='contact'),
    path('skills/', views.skills_view, name='skills'),
    path('social-media-links/', views.social_media_links_view, name='social-media-links'),
    path('work-experience/', views.work_experience_list, name='work_experience_list'),
    path('exam-cracked/', views.exam_cracked_list, name='exam_cracked_list'),
    path('participation-certificates/', views.participation_certificate_list, name='participation_certificate_list'),
    path('other-skills/', views.other_skill_list, name='other_skill_list'),
    path('gallery-images/', views.gallery_image_list, name='gallery-images'),
]

