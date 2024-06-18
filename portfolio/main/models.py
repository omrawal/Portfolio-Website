from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self) -> str:
        return self.name
    
class Project(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200,null=True)
    description = models.TextField()
    tags = models.ManyToManyField(Tag,related_name='projects')
    link = models.URLField(max_length=200,blank=True)
    rank = models.IntegerField(default=10)
    def __str__(self) -> str:
        return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey(Project,related_name='images',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images/')

    def __str__(self) -> str:
        return f"{self.project.title} Image"

class ProfilePicture(models.Model):
    image = models.ImageField(upload_to='profile_picture/')

class Resume(models.Model):
    resume = models.URLField(max_length=200,blank=True)

class Skill(models.Model):
    skill_title = models.CharField(max_length=200)
    skill_logo_link = models.URLField(max_length=200,blank=True)
    rank = models.IntegerField(default=10)
    def __str__(self) -> str:
        return self.skill_title

class Experience(models.Model):
    company_name = models.CharField(max_length=200)
    company_logo_link = models.URLField(max_length=200,blank=True)
    company_website_link = models.URLField(max_length=200,blank=True)
    designation = models.CharField(max_length=200)
    description = models.TextField(null=True)
    tools = models.TextField(null=True)
    period_and_location = models.CharField(max_length=200) # Dec 2018 - July 2019 | Ahmedabad, India
    rank = models.IntegerField(default=10)
    def __str__(self) -> str:
        return f"{self.company_name},{self.designation},{self.period_and_location}"
    
class About(models.Model):
    headline = models.TextField()
    languages = models.TextField()
    databases = models.TextField()
    libraries = models.TextField()
    frameworks = models.TextField()
    tools_and_tech = models.TextField()
    def __str__(self) -> str:
        return f"About Content"