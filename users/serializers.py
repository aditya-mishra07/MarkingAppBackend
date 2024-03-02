from rest_framework import serializers
from rest_framework.response import Response
from .models import *

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'
        read_only_fields = ('id',)

class StudentReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        depth = 2
        fields = '__all__'
        read_only_fields = ('id',)


class FacultySerializer(serializers.ModelSerializer):

    class Meta:
        model = Faculty
        fields = '__all__'
        read_only_fields = ('id',)

class FacultyReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Faculty
        depth = 2
        fields = '__all__'
        read_only_fields = ('id',)

class ConvenorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Convenor
        fields = '__all__'
        read_only_fields = ('id',)

class ConvenorReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Convenor
        depth = 2
        fields = '__all__'
        read_only_fields = ('id',)

class FacultyRoleAcademicSerializer(serializers.ModelSerializer):

    class Meta:
        model = FacultyRoleAcademic
        fields = '__all__'
        read_only_fields = ('id',)


class FacultyRoleAcademicReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = FacultyRoleAcademic
        depth = 2
        fields = '__all__'
        read_only_fields = ('id',)


class FacultyRoleModeratorSerializer(serializers.ModelSerializer):

    class Meta:
        model = FacultyRoleModerator
        fields = '__all__'
        read_only_fields = ('id',)

class FacultyRoleModeratorReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = FacultyRoleModerator
        depth = 2
        fields = '__all__'
        read_only_fields = ('id',)

class ProjectAssignmentStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectAssignmentStatus
        fields = '__all__'
        read_only_fields = ('id',)

class ProjectAssignmentStatusReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectAssignmentStatus
        depth = 2
        fields = '__all__'
        read_only_fields = ('id',)

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ('id',)

class ProjectReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        depth = 2
        fields = '__all__'
        read_only_fields = ('id',)

class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = '__all__'
        read_only_fields = ('id',)

class RoleReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        depth = 2
        fields = '__all__'
        read_only_fields = ('id',)

class MarkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mark
        fields = '__all__'
        read_only_fields = ('id',)

class MarkReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mark
        depth = 2
        fields = '__all__'
        read_only_fields = ('id',)

class FinalMarkSerializer(serializers.ModelSerializer):

    class Meta:
        model = FinalMark
        fields = '__all__'
        read_only_fields = ('id',)

class FinalMarkReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = FinalMark
        depth = 2
        fields = '__all__'
        read_only_fields = ('id',)
