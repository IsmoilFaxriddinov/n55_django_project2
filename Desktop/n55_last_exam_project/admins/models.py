from django.db import models
from django.contrib.auth.models import User

class SuperAdminModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class AdminModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(SuperAdminModel, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class TeacherModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    managed_by = models.ForeignKey(AdminModel, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class StudentModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    managed_by = models.ForeignKey(AdminModel, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class GroupModel(models.Model):
    name = models.CharField(max_length=100)
    admin = models.ForeignKey(AdminModel, on_delete=models.CASCADE)
    teachers = models.ManyToManyField(TeacherModel, blank=True)
    students = models.ManyToManyField(StudentModel, blank=True)

    def __str__(self):
        return self.name

class HomeworkModel(models.Model):
    title = models.CharField(max_length=200)
    teacher = models.ForeignKey(TeacherModel, on_delete=models.CASCADE)
    group = models.ForeignKey(GroupModel, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title