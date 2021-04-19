from django.urls import path
from .views import *
urlpatterns = [
    path('prof/', profGetAdd),
    path('prof/<uuid:pid>', profEditDelete),
    path('student/', studentGetAdd),
    path('student/<uuid:sid>', studentEditDelete),
    path('subject/', subjectGetAdd),
    path('subject/<uuid:sid>', subjectEditDelete),
    path('class/', classGetAdd),
    path('class/<uuid:cid>', classEditDelete),
    path('note/', noteGetAdd),
    path('note/<uuid:nid>', noteEditDelete),
]