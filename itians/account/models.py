from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=255)  
    email = models.EmailField(default='hel@gmail.com')
    password = models.CharField(max_length=255, default='password')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    traineeobj = models.ForeignKey("trainee.Trainee", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
