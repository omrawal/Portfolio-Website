from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self) -> str:
        return self.name
    
class Project(models.Model):
    title = models.CharField(max_length=200)
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