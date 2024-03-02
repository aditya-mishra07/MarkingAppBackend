# app/movies/urls.py

from django.urls import path

from .views import *

urlpatterns = [
    path("api/students/", StudentList.as_view()),
    path("api/student/<int:pk>/", StudentList.as_view(),name='students-single'),
    path("api/facultys/", FacultyList.as_view()),
    path("api/faculty/<int:pk>/", FacultyList.as_view(),name='faculty-single'),
    path("api/projects/", ProjectList.as_view()),
    path("api/project/<int:pk>/", ProjectList.as_view(),name='projects-single'),
    path("api/roles/", RoleList.as_view()),
    path("api/role/<int:pk>/", RoleList.as_view(),name='role-single'),
    path("api/academics/", FacultyRoleAcademicList.as_view(),name='academic-list'),
    path("api/academic/<int:pk>/", FacultyRoleAcademicList.as_view(),name='academic-single'),
    path("api/moderator/<int:pk>/", FacultyRoleModeratorList.as_view(),name='moderator-single'),
    path("api/moderators/", FacultyRoleModeratorList.as_view(),name='moderator-list'),
    path("api/marks/", MarkList.as_view()),
    path("api/mark/<int:pk>/", MarkList.as_view(),name='mark-single'),
    path("api/finalmarks/", FinalMarkList.as_view()),
    path("api/finalmark/<int:pk>/", FinalMarkList.as_view(),name='finalmark-single'),
    path("api/projectassignmentstatuses/", ProjectAssignmentStatusList.as_view()),
    path("api/projectassignmentstatus/<int:pk>/", ProjectAssignmentStatusList.as_view(),name='projectassignmentstatus-single'),
    path("api/convenores/", ConvenorList.as_view()),
    path("api/convenor/<int:pk>/", ConvenorList.as_view(),name='convenor-single'),
    # path("api/project/:id/academics", StudentList.as_view()),
    # path("api/project/:id/moderators", StudentList.as_view()),
    # path("api/student/:id/project/:id/moderators", StudentList.as_view()),
    # path("api/student/:id/project/:id/moderators/:id/mark", StudentList.as_view()),

]
