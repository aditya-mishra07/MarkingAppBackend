# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
# from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# #Creating role instances
# student_role = Role.objects.create(name='Student')
# convenor_role = Role.objects.create(name='Convenor')
# maker_role = Role.objects.create(name='Maker')
# moderator_role = Role.objects.create(name='Moderator')


class Project(models.Model):
    name = models.CharField(max_length=100)
    description=models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Student(models.Model):
	first_name=models.CharField(max_length=100)
	last_name=models.CharField(max_length=100)
	email=models.CharField(max_length=100,unique=True)
	interested_category=models.CharField(max_length=100,blank=True,null=True)
	verify_status=models.BooleanField(default=False)


	def __str__(self):
		return f"{self.first_name} - {self.last_name}"

	# # Total Enrolled Courses
	# def enrolled_projects(self):
	# 	enrolled_projects=StudentProjectEnrollment.objects.filter(student=self).count()
	# 	return enrolled_courses

	# # Completed assignments
	# def complete_projects(self):
	# 	complete_projects=StudentAssignment.objects.filter(student=self,student_status=True).count()
	# 	return complete_assignments

	# # Pending assignments
	# def pending_project(self):
	# 	pending_assignments=StudentAssignment.objects.filter(student=self,student_status=False).count()
	# 	return pending_assignments

	# class Meta:
	# 	verbose_name_plural="5. Students"

# {
# "first_name": "aditya",
# "last_name": "mishra",
# "email": "mishra.adi2005@gmail.com",
# "interested_category": "aiprojects",
# "verify_status": "False"
# }

class Faculty(models.Model):
	first_name=models.CharField(max_length=100)
	last_name=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	password=models.CharField(max_length=100,blank=True,null=True)
	qualification=models.CharField(max_length=200)
	skills=models.TextField()
	verify_status=models.BooleanField(default=False)

	class Meta:
		verbose_name_plural="Faculty"

	def skill_list(self):
		skill_list=self.skills.split(',')
		return skill_list

# Total Teacher Students
	def total_teacher_students(self):
		total_students=ProjectAssignmentStatus.objects.filter(total_students=self).count()
		return total_students
	def __str__(self):
		return f"{self.first_name} - {self.last_name}"



class Convenor(models.Model):
	first_name=models.CharField(max_length=100)
	last_name=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	password=models.CharField(max_length=100,blank=True,null=True)
	qualification=models.CharField(max_length=200)
	skills=models.TextField()
	verify_status=models.BooleanField(default=False)


	class Meta:
		verbose_name_plural="Convenor"

	def skill_list(self):
		skill_list=self.skills.split(',')
		return skill_list


# class UserRole(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     role = models.ForeignKey(Role, on_delete=models.CASCADE)
#     def __str__(self):
#         return f"{self.user.email} - {self.role.name} - {self.project.name}"
#

class FacultyRoleAcademic(models.Model):
    username = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    faculty_role = models.ForeignKey(Role, on_delete=models.CASCADE)
    project=models.ForeignKey(Project, on_delete=models.CASCADE)
    #
    # def __str__(self):
    #     return f"{self.username.user.email} - {self.user.role} - {self.user.project} - {self.maker.email}"


class FacultyRoleModerator(models.Model):
    username = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    moderator_role = models.ForeignKey(Role, on_delete=models.CASCADE)
    project=models.ForeignKey(Project, on_delete=models.CASCADE)
    #
    # def __str__(self):
    #     return f"{self.username.user.email} - {self.user.role} - {self.user.project} - {self.maker.email}"



class ProjectAssignmentStatus(models.Model):
      student = models.ForeignKey(Student, on_delete=models.CASCADE)
      project=models.ForeignKey(Project, on_delete=models.CASCADE)
      project_submission_date=models.DateField(null=True,blank=True)
      project_target_completion_date=models.DateField(null=True,blank=True)
      project_submission_status=models.BooleanField(default=False)
      project_issue_date=models.DateField(auto_now_add=True, null=True,blank=True)
      list_of_academics=models.ManyToManyField('FacultyRoleAcademic',blank=True)
      moderator=models.ForeignKey(FacultyRoleModerator,on_delete=models.CASCADE,null=True,blank=True)

class Mark(models.Model):
    academics = models.ForeignKey(FacultyRoleAcademic, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    mark = models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    verify_status=models.BooleanField(default=False)

class FinalMark(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    finalmark = models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)

    # def __str__(self):
    #     return f"{self.username.user.email} - {self.user.role} - {self.user.project} - {self.moderator.email}"
#20-11-39
