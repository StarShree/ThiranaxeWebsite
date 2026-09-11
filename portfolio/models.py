from django.db import models


class Profile(models.Model):
    full_name = models.CharField(max_length=100, default="Alex Mercer")
    tagline = models.CharField(max_length=200, default="Full Stack Engineer & Cloud Architect")
    bio = models.TextField(
        default="Passionate Full-Stack Developer specializing in building high-performance web applications with Django, Python, React, and Google Cloud Platform."
    )
    about_details = models.TextField(
        default="With hands-on experience designing robust relational databases, scalable microservices, and sleek user experiences, I turn complex technical challenges into elegant, production-grade solutions."
    )
    years_of_experience = models.PositiveIntegerField(default=3)
    completed_projects_count = models.PositiveIntegerField(default=18)
    happy_clients_count = models.PositiveIntegerField(default=14)
    location = models.CharField(max_length=100, default="Bangalore, India")
    email = models.EmailField(default="developer@example.com")
    phone = models.CharField(max_length=30, blank=True, default="+91 98765 43210")
    github_url = models.URLField(blank=True, default="https://github.com")
    linkedin_url = models.URLField(blank=True, default="https://linkedin.com")
    twitter_url = models.URLField(blank=True, default="https://twitter.com")
    resume_url = models.URLField(blank=True, default="#")
    avatar_url = models.URLField(
        blank=True,
        default="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=600&q=80"
    )
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


class SkillCategory(models.Model):
    name = models.CharField(max_length=60)
    icon = models.CharField(max_length=50, default="code")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = "Skill Categories"
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    proficiency = models.PositiveIntegerField(default=85, help_text="Proficiency percentage (0-100)")
    icon_class = models.CharField(max_length=50, blank=True, help_text="FontAwesome or Lucide icon class")
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-proficiency']

    def __str__(self):
        return f"{self.name} ({self.proficiency}%)"


class Project(models.Model):
    CATEGORY_CHOICES = [
        ('all', 'All'),
        ('fullstack', 'Full Stack'),
        ('cloud', 'Cloud & DevOps'),
        ('backend', 'Backend & API'),
        ('frontend', 'Frontend UI'),
        ('gamedev', 'Game Dev'),
    ]

    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=160, unique=True)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='fullstack')
    short_description = models.CharField(max_length=255)
    full_description = models.TextField()
    tech_stack = models.CharField(max_length=255, help_text="Comma-separated technologies, e.g. Django, MySQL, React")
    image_url = models.URLField(
        default="https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800&q=80"
    )
    live_demo_url = models.URLField(blank=True, default="#")
    github_url = models.URLField(blank=True, default="https://github.com")
    is_featured = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

    @property
    def tech_list(self):
        return [tech.strip() for tech in self.tech_stack.split(',') if tech.strip()]


class Experience(models.Model):
    role = models.CharField(max_length=120)
    company = models.CharField(max_length=120)
    location = models.CharField(max_length=100, blank=True, default="Bangalore, India")
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50, default="Present")
    description = models.TextField()
    technologies = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return f"{self.role} at {self.company}"


class Education(models.Model):
    degree = models.CharField(max_length=150)
    institution = models.CharField(max_length=150)
    period = models.CharField(max_length=50)
    grade_or_details = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = "Education"
        ordering = ['order', 'id']

    def __str__(self):
        return f"{self.degree} - {self.institution}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Message from {self.name}: {self.subject}"
