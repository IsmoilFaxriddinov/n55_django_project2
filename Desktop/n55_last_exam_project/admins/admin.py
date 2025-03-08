from django.contrib import admin

from admins.models import AdminModel, GroupModel, HomeworkModel, StudentModel, SuperAdminModel, TeacherModel

admin.site.register(SuperAdminModel)
admin.site.register(AdminModel)
admin.site.register(GroupModel)
admin.site.register(TeacherModel)
admin.site.register(HomeworkModel)
admin.site.register(StudentModel)
