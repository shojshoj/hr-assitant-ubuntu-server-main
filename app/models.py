from pickle import TRUE
from django.db import models

GENDER_CHOICES = [
    ('Male' , 'Male'),
    ('Female' , 'Female'),
]
POSITION = [
    ('Trainee' , 'Trainee'),
    ('Senior Developer' , 'Senior Developer'),
    ('Junior Developer' , 'Junior Developer'),
    ('Network Support Specialist' , 'Network Support Specialist'),
    ('System Analyst' , 'System Analyst'),
    ('User Experience Designer' , 'User Experience Designer'),
    ('Data Scientist' , 'Data Scientist'),
    ('Database Administrator' , 'Database Administrator'),
]
EMP_TYPE = {
    ('Full-Time' , 'Full-Time'),
    ('Part-time' , 'Part-time'),
    ('Temporary' , 'Temporary'),
    ('Seasonal' , 'Seasonal'),
}
STATUS = {
    ('Active' , 'Active'),
    ('On-Leave' , 'On-Leave'),
    ('Suspended' , 'Suspended'),
    ('Terminated' , 'Terminated'),
}
class Employee(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    mobile = models.CharField(max_length=15)
    image = models.ImageField(default="HR.png", null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=True)
    position = models.CharField(max_length=50, choices=POSITION, null=True)
    emp_type = models.CharField(max_length=20, choices=EMP_TYPE, null=True)
    status = models.CharField(max_length=20, choices=STATUS, null=True)
    date_created = models.DateField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.firstname
