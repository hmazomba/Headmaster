from django.db import models

from administrators.models import Semester

# Create your models here.

class User_Roles(AbstractUser):
    role = ((1, "Admin"), (2, "Teacher"), (3, "Student"))
    user_roles = models.CharField(max_length=50, default=1, choices=roles)
    
    def __str__(self):
        full_name = self.first_name + " " + self.last_name #first and last name fields are built in Django fields
        return full_name



class Institute(models.Model):
    name = models.CharField(max_length=50)
    date_established = models.DateField(auto_now=False, auto_now_add=False)
    email = models.EmailField(max_length=254)
    website = models.CharField(max_length=150)
    mobile = models.CharField(max_length=150)
    telephone = models.CharField(max_length=150)
    address = models.TextField()
    logo = models.FileField(upload_to=institute/images, max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, auto_now_add=True)
    objects = models.Manager()
    
    def __str__(self):
        #returns the school's name
        return self.name 
    
    
class Admin(models.Model):
    #Will use one to one relationship between admins, teachers and students with the user manager model
    role = models.OneToOneField(User_Roles,on_delete=models.CASCADE)
    created_at = models.DateField(auto_now=True, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=True)
    objects= models.Manager()
    
    
class Gender(models.Model):
    name = models.CharField(max_length= 30)
    created_at = models.DateField(auto_now=True, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=True) 
    objects = models.Manager()
    
    def __str__(self):
        return self.name
    
     
class Classes(models.Model):
    name = models.CharField(max_length=100)   
    code = models.CharField(max_length=150)
    created_at = models.DateField(auto_now=True, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=True) 
    objects = models.Manager()
    
    def __str__(self):
        return self.name
    
    
class Country(models.Model):
    name = models.CharField(max_length=100)   
    code = models.CharField(max_length=150)
    created_at = models.DateField(auto_now=True, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=True) 
    objects = models.Manager()
    
    def __str__(self):
        return self.name


class Faculties(models.Model):
    faculty_name = models.CharField(max_length=100)   
    faculty_code = models.CharField(max_length=150)
    faculty_status = models.BooleanField(default=False)
    created_at = models.DateField(auto_now=True, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=True) 
    objects = models.Manager()
    
    def __str__(self):
        return self.faculty_name


class Departments(models.Model):
    department_name = models.CharField(max_length=100)   
    department_code = models.CharField(max_length=150)
    department_status = models.BooleanField(default=False)
    department_description = models.TextField()
    created_at = models.DateField(auto_now=True, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=True) 
    objects = models.Manager()
    
    def __str__(self):
        return self.department_name    


class Teachers(models.Model):
    role = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now=True, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=True) 
    objects = models.Manager()
    
    def __str__(self):
        
        if self.role.first_name and self.role.lasty_name:
            full_name = self.role.first_name + " " + self.role.last_name #first and last name fields are built in Django fields
        return full_name
    
    


class TeacherProfile(models.Model):
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    name = models.ForeignKey(Gender, on_delete=models.CASCADE)
    nationality= models.ForeignKey(Country, on_delete=models.CASCADE)    
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=50)
    image = models.FileField(upload_to=teachers/images, blank=True, null=True, max_length=100)   
    created_at = models.DateField(auto_now=True, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=True) 
    objects = models.Manager()
    
    def __str__(self):
        return self.teacher.email
    
 
class Courses(models.Model):
    course_name = models.CharField(max_length=150)
    course_code = models.CharField(max_length=150)    
    faculty = models.ForeignKey(Faculties, on_delete=models.CASCADE)
    department = models.ForeignKey(Departments,on_delete=models.CASCADE)
    created_at = models.DateField(auto_now=True, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=True) 
    objects = models.Manager()
    
    def __str__(self):
        return self.course_name
    
class Shifts(models.Model):
    shift = models.CharField(max_length=150)
    created_at = models.DateField(auto_now=True, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=True) 
    objects = models.Manager()
    
    def __str__(self):
        return self.shift
    

class GPA(models.Model):
    gpa_for = models.CharField(max_length=150)
    gpa = models.CharField(max_length=150)    
    grade= models.FloatField(8, 2)
    mark_from = models.IntegerField()
    mark_to = models.IntegerField()
    created_at = models.DateField(auto_now=True, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=True) 
    objects = models.Manager()
    
    def __str__(self):
        return self.grade
    
class Academics(models.Model):
    academic_year = models.CharField(max_length=150)
    academic_status = models.BooleanField(default=False)   
    created_at = models.DateField(auto_now=True, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=True) 
    objects = models.Manager()
    
    def __str__(self):
        return self.academic_year
    


class Subjects(models.Model):
    subject_name = models.CharField(max_length=150)
    subject_code = models.CharField(max_length=150)
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculties, on_delete=models.CASCADE)
    departments = models.ForeignKey(Departments, on_delete=models.CASCADE)
    subjects_total = models.IntegerField()    
    created_at = models.DateField(auto_now=True, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=True) 
    objects = models.Manager()
    
    def __str__(self):
        return self.subject_name
    
    def get_total_subjects(self):
        tot = 0 
        total = Subjects.objects.all()
        for i in total:
            tot += i
        return i    
    

class Session(models.Model):
    session = models.CharField(max_length=150, unique=True)
    is_current_session = models.BooleanField(default = False)    
    created_at = models.DateField(auto_now=True, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=True) 
    objects = models.Manager()
    
    def __str__(self):
        return self.session
       
class Semester(models.Model):
    semester_name = models.CharField(max_length=150)
    is_current_semester = models.BooleanField(default = False)
    semester_code = models.CharField(max_length=100)
    semester_duration = models.CharField(max_length=100)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    next_semester_begins = models.DateField(auto_now=False, auto_now_add=False, null=True)    
    created_at = models.DateField(auto_now=True, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=True) 
    objects = models.Manager()
    
    def __str__(self):
        return self.semester_name
    

class Levels(models.Model):
    level = models.CharField(max_length=150)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculties, on_delete=models.CASCADE)
    departments = models.ForeignKey(Departments, on_delete=models.CASCADE)
    next_semester_begins = models.DateField(auto_now=False, auto_now_add=False, null=True)    
    created_at = models.DateField(auto_now=True, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=True) 
    objects = models.Manager()
    
    def __str__(self):
        return self.semester_name                  
