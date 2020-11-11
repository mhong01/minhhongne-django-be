from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(auto_created= True, primary_key=True, serialize=True, verbose_name='ID')
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.CharField(max_length=80)
    # login_id = models.IntegerField()
    def __str__(self):
        return self.email

class Award (models.Model):
    award_id = models.AutoField(auto_created= True, primary_key=True, serialize=True, verbose_name='ID')
    event = models.CharField(max_length=255)
    award_name = models.CharField(max_length=255)
    award_year = models.CharField(max_length=5)
    description = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name='awards', on_delete=models.DO_NOTHING,db_constraint=False)

    def __str__(self):
        return self.award_name

class ContactInfo(models.Model):
    contact_id = models.AutoField(auto_created= True, primary_key = True, serialize=True)
    address = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=255)
    github = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name='info', on_delete=models.DO_NOTHING,db_constraint=False)

    def __str__(self):
        return self.email

class Education (models.Model):
    edu_id = models.AutoField(auto_created= True, primary_key = True, serialize=True)
    school_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    program = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name='educations', on_delete=models.DO_NOTHING,db_constraint=False)

    def __str__(self):
        return self.program

class Experience (models.Model):
    exp_id = models.AutoField(auto_created= True, primary_key = True, serialize=True)
    user = models.ForeignKey(User, related_name='experiences', on_delete=models.DO_NOTHING,db_constraint=False)
    role = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    overview = models.CharField(max_length=255)

    def __str__(self):
        return self.company

class Project_Experience (models.Model):
    project_id = models.AutoField(auto_created= True, primary_key = True, serialize=True)
    exp = models.ForeignKey(Experience, related_name='projects', on_delete=models.DO_NOTHING,db_constraint=False)
    name = models.CharField(max_length=255)
    overview = models.CharField(max_length=255)
    duties = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Skill (models.Model):
    skill_id = models.AutoField(auto_created=True, primary_key=True, serialize=True)
    user = models.ForeignKey(User, related_name='skills', on_delete=models.DO_NOTHING,db_constraint=False)
    skill_name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.skill_name