from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.

# ---- Start of User Profile Models ---- #
class CustomUserProfileModels(AbstractUser):
    picture = models.ImageField(
        upload_to='images/', 
        default='images/default.png', 
        verbose_name='Foto Anggota', 
        blank=True, 
        null=True
    )
    
    def __str__(self):
        return self.username
# ---- End of User Profile Models ---- #

# ---- Start of Project Models ---- #
class ProjekModels(models.Model):
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name='projects',
        verbose_name="Project Owner"
    )

    STATUS_PROJEK = [
        ('berlangsung', 'Berlangsung'),
        ('selesai', 'Selesai'),
        ('gagal', 'Gagal')
    ]
    
    projectname = models.CharField(
        max_length=255, 
        verbose_name="Nama Projek")
    
    pic = models.CharField(
        max_length=255, 
        verbose_name="PiC (Person in Charge)")
    
    clientname = models.CharField(
        max_length=255, 
        verbose_name="Nama Client")
    
    status = models.CharField(
        max_length=20,
        choices=STATUS_PROJEK,
        default='berlangsung',
        verbose_name='Status Projek'
    )

    # Add this to your ProjekModels class
    def get_progress_percentage(self):
        if hasattr(self, 'objective') and self.objective:
            obj = self.objective
            if obj.date_start and obj.date_end:
                total_days = (obj.date_end - obj.date_start).days
                if total_days > 0:
                    days_passed = (timezone.now().date() - obj.date_start).days
                    percentage = min(100, max(0, (days_passed / total_days) * 100))
                    return round(percentage)
        return 0

    def __str__(self):
        return self.projectname

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
# ---- End of Project Models ---- #

# ---- Start of Meaningful Objectives Models ---- #
class ObjectiveModels(models.Model):  
    project = models.OneToOneField(
        ProjekModels,
        on_delete=models.CASCADE,
        related_name='objective',
        verbose_name='Related Project'
    )

    organizational = models.TextField(verbose_name='Organizational Objectives')
    leading_indicators = models.TextField(verbose_name='Leading Indicators')
    user_outcomes = models.TextField(verbose_name='User Outcomes')
    model_properties = models.TextField(verbose_name='Model Properties')
    date_start = models.DateField(null=True, blank=True, verbose_name='Tanggal Mulai')
    date_end = models.DateField(null=True, blank=True, verbose_name='Tanggal Selesai')

    class Meta:
        verbose_name = "Meaningful Objective"
        verbose_name_plural = "Meaningful Objectives"
# ---- End of Meaningful Objectives Models ---- #

# ---- Start of Intelligence Experience Models ---- #
class ExperienceModels(models.Model):  
    project = models.OneToOneField(
        ProjekModels,
        on_delete=models.CASCADE,
        related_name='experience',
        verbose_name='Related Project'
    )

    automate = models.TextField(verbose_name='Automate')
    prompt = models.TextField(verbose_name='Prompt')
    annotate = models.TextField(verbose_name='Annotate')
    organization = models.TextField(verbose_name='Organization')
    system_objectives = models.TextField(verbose_name='System Objectives')
    minimize_flaws = models.TextField(verbose_name='Minimize Intelligence Flaws')
    create_data = models.TextField(verbose_name='Create data to grow')

    class Meta:
        verbose_name = "Intelligence Experience"
        verbose_name_plural = "Intelligence Experiences"
# ---- End of Intelligence Experience Models ---- #

# ---- Start of Intelligence Implementation Models ---- #
class ImplementationModels(models.Model):  
    project = models.OneToOneField(
        ProjekModels,
        on_delete=models.CASCADE,
        related_name='implementation',
        verbose_name='Related Project'
    )

    business_process = models.TextField(verbose_name='Business Process')
    technology = models.TextField(verbose_name='Used Technology')
    build_process = models.TextField(verbose_name='Built Process')

    class Meta:
        verbose_name = "Intelligence Implementation"
        verbose_name_plural = "Intelligence Implementations"
# ---- End of Intelligence Implementation Models ---- #

# ---- Start of Limitation Models ---- #
class LimitationModels(models.Model):  
    project = models.OneToOneField(
        ProjekModels,
        on_delete=models.CASCADE,
        related_name='limitation',
        verbose_name='Related Project'
    )
    
    limitation = models.TextField(verbose_name='Limitation')

    class Meta:
        verbose_name = "Limitation"
        verbose_name_plural = "Limitations"
# ---- End of Limitation Models ---- #

# ---- Start of Realization Models ---- #
class RealizationModels(models.Model):
    project = models.OneToOneField(
        ProjekModels,
        on_delete=models.CASCADE,
        related_name='realization',
        verbose_name='Related Project'
    )

    realization = models.TextField(verbose_name='Realization')

    class Meta:
        verbose_name = 'Realization'
        verbose_name_plural = 'Realizations'
# ---- End of Realization Models ---- #

# ---- Start of Planning Models ---- #
class PlanningModels(models.Model):
    project = models.OneToOneField(
        ProjekModels,
        on_delete=models.CASCADE,
        related_name='planning',
        verbose_name='Related Project'
    )

    deployment = models.TextField(verbose_name='Deployment')
    maintenance = models.TextField(verbose_name='Maintenance')
    operating = models.TextField(verbose_name='Operating System')

    class Meta:
        verbose_name = 'Planning'
        verbose_name_plural = 'Plannings'
# ---- End of Planning Models ---- #