from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *

class StudentList(APIView):
    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request,pk=None,format=None):
        if pk is not None:
             project = Student.objects.get(pk=pk)
             serializer = StudentReadSerializer(project)
             return Response(serializer.data)
        else:
            students = Student.objects.all()
            serializer = StudentReadSerializer(students, many=True)
            return Response(serializer.data)

    def put(self, request, pk=None):  # Add 'pk=None' to the put method
        if pk is not None:
            book = Student.objects.get(pk=pk)
            serializer = StudentSerializer(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Please provide a valid Moderator ID.'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):  # Add 'pk=None' to the delete method
        if pk is not None:
            book = Student.objects.get(pk=pk)
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            books = Student.objects.all()
            books.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class FacultyList(APIView):
    def post(self, request, format=None):
        serializer = FacultySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request,pk=None,format=None):
        if pk is not None:
             project = Faculty.objects.get(pk=pk)
             serializer = FacultyReadSerializer(project)
             return Response(serializer.data)
        else:
            faculty = Faculty.objects.all()
            serializer = FacultyReadSerializer(faculty, many=True)
            return Response(serializer.data)

    def put(self, request, pk=None):  # Add 'pk=None' to the put method
        if pk is not None:
            book = Faculty.objects.get(pk=pk)
            serializer = FacultySerializer(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Please provide a valid Moderator ID.'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):  # Add 'pk=None' to the delete method
        if pk is not None:
            book = Faculty.objects.get(pk=pk)
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            books = Faculty.objects.all()
            books.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class ProjectList(APIView):
    def post(self, request, format=None):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request,pk=None,format=None):
        if pk is not None:
             project = Project.objects.get(pk=pk)
             serializer = ProjectReadSerializer(project)
             return Response(serializer.data)
        else:
            project = Project.objects.all()
            serializer = ProjectReadSerializer(project, many=True)
            return Response(serializer.data)

    def put(self, request, pk=None):  # Add 'pk=None' to the put method
        if pk is not None:
            book = Project.objects.get(pk=pk)
            serializer = ProjectSerializer(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Please provide a valid Moderator ID.'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):  # Add 'pk=None' to the delete method
        if pk is not None:
            book = Project.objects.get(pk=pk)
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            books = Project.objects.all()
            books.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class RoleList(APIView):
    def post(self, request, format=None):
        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request,pk=None,format=None):
        if pk is not None:
             project = Role.objects.get(pk=pk)
             serializer = RoleReadSerializer(project)
             return Response(serializer.data)
        else:
            role = Role.objects.all()
            serializer = RoleReadSerializer(role, many=True)
            return Response(serializer.data)
    def put(self, request, pk=None):  # Add 'pk=None' to the put method
        if pk is not None:
            book = Role.objects.get(pk=pk)
            serializer = RoleSerializer(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Please provide a valid Moderator ID.'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):  # Add 'pk=None' to the delete method
        if pk is not None:
            book = Role.objects.get(pk=pk)
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            books = Role.objects.all()
            books.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class FacultyRoleAcademicList(APIView):
    def post(self, request, format=None):
        serializer = FacultyRoleAcademicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request,pk=None,format=None):
        if pk is not None:
             project = FacultyRoleAcademic.objects.get(pk=pk)
             serializer = FacultyRoleAcademicReadSerializer(project)
             return Response(serializer.data)
        else:
             project = FacultyRoleAcademic.objects.all()
             serializer = FacultyRoleAcademicReadSerializer(project, many=True)
             return Response(serializer.data)

    def put(self, request, pk=None):  # Add 'pk=None' to the put method
        if pk is not None:
            book = FacultyRoleAcademic.objects.get(pk=pk)
            serializer = FacultyRoleAcademicSerializer(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Please provide a valid Moderator ID.'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):  # Add 'pk=None' to the delete method
        if pk is not None:
            book = FacultyRoleAcademic.objects.get(pk=pk)
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            books = FacultyRoleAcademic.objects.all()
            books.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class FacultyRoleModeratorList(APIView):
    def post(self, request, format=None):
        serializer = FacultyRoleModeratorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request,pk=None,format=None):
        if pk is not None:
             project = FacultyRoleModerator.objects.get(pk=pk)
             serializer = FacultyRoleModeratorReadSerializer(project)
             return Response(serializer.data)
        else:
             project = FacultyRoleModerator.objects.all()
             serializer = FacultyRoleModeratorReadSerializer(project, many=True)
             return Response(serializer.data)

    def put(self, request, pk=None):  # Add 'pk=None' to the put method
        if pk is not None:
            book = FacultyRoleModerator.objects.get(pk=pk)
            serializer = FacultyRoleModeratorSerializer(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Please provide a valid Moderator ID.'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):  # Add 'pk=None' to the delete method
        if pk is not None:
            book = FacultyRoleModerator.objects.get(pk=pk)
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            books = FacultyRoleModerator.objects.all()
            books.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)



class ConvenorList(APIView):
    def post(self, request, format=None):
        serializer = ConvenorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request,pk=None,format=None):
        if pk is not None:
             project = Convenor.objects.get(pk=pk)
             serializer = ConvenorReadSerializer(project)
             return Response(serializer.data)
        else:
            project = Convenor.objects.all()
            serializer = ConvenorReadSerializer(project, many=True)
            return Response(serializer.data)

    def put(self, request, pk=None):  # Add 'pk=None' to the put method
        if pk is not None:
            book = Convenor.objects.get(pk=pk)
            serializer = ConvenorSerializer(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Please provide a valid Moderator ID.'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):  # Add 'pk=None' to the delete method
        if pk is not None:
            book = Convenor.objects.get(pk=pk)
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            books = Convenor.objects.all()
            books.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class ProjectAssignmentStatusList(APIView):
    def post(self, request, format=None):
        serializer = ProjectAssignmentStatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request,pk=None,format=None):
        if pk is not None:
             project = ProjectAssignmentStatus.objects.get(pk=pk)
             serializer = ProjectAssignmentStatusReadSerializer(project)
             return Response(serializer.data)
        else:
            project = ProjectAssignmentStatus.objects.all()
            serializer = ProjectAssignmentStatusReadSerializer(project, many=True)
            return Response(serializer.data)

    def put(self, request, pk=None):  # Add 'pk=None' to the put method
        if pk is not None:
            book = ProjectAssignmentStatus.objects.get(pk=pk)
            serializer = ProjectAssignmentStatusSerializer(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Please provide a valid Moderator ID.'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):  # Add 'pk=None' to the delete method
        if pk is not None:
            book = ProjectAssignmentStatus.objects.get(pk=pk)
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            books = ProjectAssignmentStatus.objects.all()
            books.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class MarkList(APIView):
    def post(self, request, format=None):
        serializer = MarkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request,pk=None,format=None):
        if pk is not None:
             project = Mark.objects.get(pk=pk)
             serializer = MarkReadSerializer(project)
             return Response(serializer.data)
        else:
            project = Mark.objects.all()
            serializer = MarkReadSerializer(project, many=True)
            return Response(serializer.data)

    def put(self, request, pk=None):  # Add 'pk=None' to the put method
        if pk is not None:
            book = Mark.objects.get(pk=pk)
            serializer = MarkSerializer(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Please provide a valid Moderator ID.'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):  # Add 'pk=None' to the delete method
        if pk is not None:
            book = FinalMark.objects.get(pk=pk)
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            books = FinalMark.objects.all()
            books.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class FinalMarkList(APIView):
    def post(self, request, format=None):
        serializer = FinalMarkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request,pk=None,format=None):
        if pk is not None:
             project = FinalMark.objects.get(pk=pk)
             serializer = FinalMarkReadSerializer(project)
             return Response(serializer.data)
        else:
            project = FinalMark.objects.all()
            serializer = FinalMarkReadSerializer(project, many=True)
            return Response(serializer.data)

    def put(self, request, pk=None):  # Add 'pk=None' to the put method
        if pk is not None:
            book = FinalMark.objects.get(pk=pk)
            serializer = FinalMarkSerializer(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Please provide a valid Moderator ID.'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):  # Add 'pk=None' to the delete method
        if pk is not None:
            book = FinalMark.objects.get(pk=pk)
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            books = FinalMark.objects.all()
            books.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
