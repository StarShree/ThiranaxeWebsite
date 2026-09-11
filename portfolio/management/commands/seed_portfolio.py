from django.core.management.base import BaseCommand
from portfolio.models import (
    Profile,
    SkillCategory,
    Skill,
    Project,
    Experience,
    Education,
    ContactMessage,
)


class Command(BaseCommand):
    help = "Seed personal portfolio data for Shriram S with updated contact, skills, and projects"

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Seeding updated portfolio data for Shriram S..."))

        # 1. Profile
        Profile.objects.all().delete()
        profile = Profile.objects.create(
            full_name="Shriram S",
            tagline="Python & Cloud Developer | Unity Game Dev & Responsive Web | Intern at Thiranex",
            bio="Enthusiastic and versatile developer well versed with Python and Cloud Computing, experienced in Ecommerce Responsive Web Design and Unity Game Development. Currently interning at Thiranex while pursuing CSE at Easwari Engineering College and a BS Degree at IIT Madras.",
            about_details=(
                "I am a passionate, multidisciplinary developer specializing in Python engineering, scalable Cloud Computing, "
                "modern Ecommerce responsive web design, and interactive Unity Game Development with C#. "
                "Currently working as an intern at Thiranex, I turn complex technical specifications into performant, elegant digital solutions. "
                "Having completed high school at Apex Pon Vidyashram, I am currently expanding my foundations through dual academic programs: "
                "Computer Science Engineering at Easwari Engineering College and the esteemed BS Degree program at IIT Madras."
            ),
            years_of_experience=2,
            completed_projects_count=14,
            happy_clients_count=10,
            location="Chennai, India",
            email="s.shriramsivakumaran@gmail.com",
            phone="9994949819",
            github_url="https://github.com/StarShree",
            linkedin_url="https://www.linkedin.com/in/shriramsss/",
            twitter_url="https://twitter.com",
            resume_url="#contact",
            avatar_url="",
            is_active=True,
        )
        self.stdout.write(self.style.SUCCESS(f"Updated Profile: {profile.full_name} ({profile.email}, {profile.phone})"))

        # 2. Skill Categories & Skills
        SkillCategory.objects.all().delete()
        Skill.objects.all().delete()

        categories_data = [
            {
                "name": "Python & Backend Engineering",
                "icon": "server",
                "order": 1,
                "skills": [
                    {"name": "Python (Core, OOP, Scripting)", "proficiency": 95, "is_featured": True},
                    {"name": "Django & Django REST Framework", "proficiency": 90, "is_featured": True},
                    {"name": "RESTful API Design & Integration", "proficiency": 88, "is_featured": True},
                    {"name": "Data Structures & Algorithmic Problem Solving", "proficiency": 85, "is_featured": False},
                ]
            },
            {
                "name": "Cloud Computing & DevOps",
                "icon": "cloud",
                "order": 2,
                "skills": [
                    {"name": "Cloud Computing Architecture & Principles", "proficiency": 92, "is_featured": True},
                    {"name": "Google Cloud Platform & Cloud Services", "proficiency": 88, "is_featured": True},
                    {"name": "Docker & Containerized Microservices", "proficiency": 84, "is_featured": True},
                    {"name": "Git & GitHub Version Control Workflows", "proficiency": 95, "is_featured": True},
                ]
            },
            {
                "name": "Unity Game Development",
                "icon": "gamepad",
                "order": 3,
                "skills": [
                    {"name": "Unity Engine (2D & 3D Game Design)", "proficiency": 88, "is_featured": True},
                    {"name": "C# Gameplay Scripting & State Machines", "proficiency": 86, "is_featured": True},
                    {"name": "Game Physics, Colliders & Raycasting", "proficiency": 84, "is_featured": True},
                    {"name": "Animation Controllers & Asset Integration", "proficiency": 82, "is_featured": False},
                ]
            },
            {
                "name": "Frontend & Ecommerce Web Design",
                "icon": "layout",
                "order": 4,
                "skills": [
                    {"name": "Ecommerce Website Responsive Design", "proficiency": 94, "is_featured": True},
                    {"name": "Modern CSS3 (Flexbox, Grid, Glassmorphism)", "proficiency": 92, "is_featured": True},
                    {"name": "HTML5 Semantic Architecture & Accessibility", "proficiency": 95, "is_featured": True},
                    {"name": "JavaScript (ES6+) & Asynchronous DOM", "proficiency": 88, "is_featured": False},
                ]
            },
            {
                "name": "Databases & Data Systems",
                "icon": "database",
                "order": 5,
                "skills": [
                    {"name": "MySQL & Relational Data Modeling", "proficiency": 90, "is_featured": True},
                    {"name": "SQL Query Optimization & Indexing", "proficiency": 86, "is_featured": True},
                    {"name": "Database Migrations & ORM Abstraction", "proficiency": 88, "is_featured": False},
                ]
            },
        ]

        for cat_info in categories_data:
            cat = SkillCategory.objects.create(
                name=cat_info["name"],
                icon=cat_info["icon"],
                order=cat_info["order"],
            )
            for s_info in cat_info["skills"]:
                Skill.objects.create(
                    category=cat,
                    name=s_info["name"],
                    proficiency=s_info["proficiency"],
                    is_featured=s_info["is_featured"],
                )
        self.stdout.write(self.style.SUCCESS("Updated Skill Categories and Skills (including Unity & Ecommerce)"))

        # 3. Projects
        Project.objects.all().delete()
        projects_data = [
            {
                "title": "Ecommerce Website Responsive Design",
                "slug": "ecommerce-website-responsive-design",
                "category": "fullstack",
                "short_description": "Full-featured, mobile-first responsive ecommerce web platform with dynamic catalogs and cart mechanics.",
                "full_description": (
                    "Engineered a responsive ecommerce web storefront designed to deliver exceptional user experiences across mobile, "
                    "tablet, and desktop viewports. Implemented optimized product showcase grids, dynamic filtering, intuitive cart interactions, "
                    "and clean semantic structure following modern UI/UX design standards."
                ),
                "tech_stack": "HTML5, CSS3, JavaScript, Responsive Design, Python",
                "image_url": "https://images.unsplash.com/photo-1522542550221-31fd19575a2d?auto=format&fit=crop&w=800&q=80",
                "live_demo_url": "#",
                "github_url": "#",
                "is_featured": True,
                "order": 1,
            },
            {
                "title": "Unity Game Dev",
                "slug": "unity-game-dev-project",
                "category": "gamedev",
                "short_description": "Interactive 2D/3D game development project engineered in Unity with C#, custom physics, and gameplay loops.",
                "full_description": (
                    "Designed and developed an engaging game experience inside the Unity Engine using C#. "
                    "Incorporates custom player movement controllers, collision and physics systems, enemy AI behaviors, "
                    "interactive environment triggers, sound design integration, and dynamic level progression."
                ),
                "tech_stack": "Unity Engine, C#, Game Physics, 2D/3D Animation, Asset Design",
                "image_url": "https://images.unsplash.com/photo-1550745165-9bc0b252726f?auto=format&fit=crop&w=800&q=80",
                "live_demo_url": "#",
                "github_url": "#",
                "is_featured": True,
                "order": 2,
            },
            {
                "title": "Cloud Computing Automated Telemetry & Monitor",
                "slug": "cloud-computing-telemetry-monitor",
                "category": "cloud",
                "short_description": "Automated server health and cloud service monitoring tool built with Python.",
                "full_description": (
                    "Developed automated monitoring scripts that track uptime, request latency, and memory footprints "
                    "across cloud instances. Built as part of cloud computing explorations with asynchronous alert dispatching."
                ),
                "tech_stack": "Python, Cloud Infrastructure, Docker, Linux, Shell Scripting",
                "image_url": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800&q=80",
                "live_demo_url": "#",
                "github_url": "https://github.com/StarShree",
                "is_featured": True,
                "order": 3,
            },
            {
                "title": "Python High-Throughput RESTful API Service",
                "slug": "python-throughput-rest-api",
                "category": "backend",
                "short_description": "Performant backend web service implementing secure token authentication, caching, and rate-limiting.",
                "full_description": (
                    "Engineered a scalable RESTful API with Django and Python. Features automated input validation, relational database indexing, "
                    "and clean layered service architecture."
                ),
                "tech_stack": "Python, Django REST, SQL, JSON, Postman",
                "image_url": "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=800&q=80",
                "live_demo_url": "#",
                "github_url": "https://github.com/StarShree",
                "is_featured": True,
                "order": 4,
            },
            {
                "title": "Cloud-Native Personal Portfolio & Showcase Engine",
                "slug": "shriram-portfolio-engine",
                "category": "fullstack",
                "short_description": "Full-stack personal portfolio system engineered with Django backend, cloud database, and dynamic glassmorphic UI.",
                "full_description": (
                    "Designed and deployed a responsive personal portfolio featuring dynamic project showcase, "
                    "AJAX contact handling, administrative control panels, and cloud data persistence. Built with clean architecture principles."
                ),
                "tech_stack": "Python, Django, Cloud Database, JavaScript, CSS3",
                "image_url": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=80",
                "live_demo_url": "#",
                "github_url": "https://github.com/StarShree",
                "is_featured": True,
                "order": 5,
            },
        ]

        for p_data in projects_data:
            Project.objects.create(**p_data)
        self.stdout.write(self.style.SUCCESS("Updated Showcase Projects (including Ecommerce & Unity Game Dev)"))

        # 4. Experience
        Experience.objects.all().delete()
        experiences_data = [
            {
                "role": "Software Development & Cloud Intern",
                "company": "Thiranex",
                "location": "Chennai / Remote",
                "start_date": "2024",
                "end_date": "Present",
                "description": (
                    "Actively engaged in software engineering workflows, backend development with Python, and cloud computing initiatives. "
                    "Collaborating on core features, optimizing application performance, and maintaining robust codebase standards."
                ),
                "technologies": "Python, Cloud Computing, Django, MySQL, Git, Linux",
                "order": 1,
            },
            {
                "role": "Python, Cloud & Game Development Specialist",
                "company": "Technical Projects & Academic Initiatives",
                "location": "Chennai, India",
                "start_date": "2023",
                "end_date": "Present",
                "description": (
                    "Well versed in Python development, scalable cloud architectures, responsive web design for ecommerce applications, "
                    "and interactive 2D/3D game design using the Unity Engine and C#."
                ),
                "technologies": "Python, Cloud Computing, Unity, C#, HTML5/CSS3, MySQL, Git",
                "order": 2,
            },
        ]

        for exp in experiences_data:
            Experience.objects.create(**exp)
        self.stdout.write(self.style.SUCCESS("Updated Work Experience entries (Thiranex)"))

        # 5. Education
        Education.objects.all().delete()
        educations_data = [
            {
                "degree": "B.E. in Computer Science and Engineering (CSE)",
                "institution": "Easwari Engineering College",
                "period": "Currently Enrolled",
                "grade_or_details": "Pursuing core Computer Science curriculum including Operating Systems, DBMS, Algorithms, and Cloud Systems.",
                "order": 1,
            },
            {
                "degree": "BS Degree in Data Science & Applications",
                "institution": "IIT Madras (IITM)",
                "period": "Currently Enrolled",
                "grade_or_details": "Premier degree program by IITM covering Python programming, mathematical foundations, data science, and modern computation.",
                "order": 2,
            },
            {
                "degree": "High School Education",
                "institution": "Apex Pon Vidyashram",
                "period": "Finished / Graduated",
                "grade_or_details": "Completed High School education with rigorous preparation in Computer Science, Mathematics, and Sciences.",
                "order": 3,
            },
        ]

        for edu in educations_data:
            Education.objects.create(**edu)
        self.stdout.write(self.style.SUCCESS("Updated Education records (Apex Pon Vidyashram, Easwari, IITM)"))

        # 6. Sample Contact Message
        ContactMessage.objects.all().delete()
        ContactMessage.objects.create(
            name="Thiranex Team",
            email="info@thiranex.com",
            subject="Welcome Shriram S!",
            message="Hi Shriram, great to see your updated ShriramPortfolio with your Ecommerce Responsive Web Design and Unity Game Dev projects!",
            is_read=True,
        )
        self.stdout.write(self.style.SUCCESS("Successfully seeded all updated portfolio data to database!"))
