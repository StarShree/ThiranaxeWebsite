from django.test import TestCase, Client
from django.urls import reverse
from portfolio.models import Profile, SkillCategory, Skill, Project, ContactMessage
import json


class PortfolioViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.profile = Profile.objects.create(
            full_name="Test Developer",
            tagline="Full Stack Engineer",
            bio="Test bio content",
            email="test@example.com"
        )
        self.cat = SkillCategory.objects.create(name="Backend", icon="server", order=1)
        self.skill = Skill.objects.create(
            category=self.cat,
            name="Django",
            proficiency=90,
            is_featured=True
        )
        self.project = Project.objects.create(
            title="Test Project",
            slug="test-project",
            category="fullstack",
            short_description="Short summary",
            full_description="Detailed description",
            tech_stack="Django, MySQL",
            is_featured=True
        )

    def test_index_page_renders_successfully(self):
        response = self.client.get(reverse('portfolio:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Developer")
        self.assertContains(response, "Full Stack Engineer")
        self.assertContains(response, "Test Project")

    def test_contact_form_submission_stores_message(self):
        post_data = {
            'name': 'Client User',
            'email': 'client@example.com',
            'subject': 'Project Consultation',
            'message': 'We would like to hire you for a Django + Cloud SQL project.'
        }
        response = self.client.post(
            reverse('portfolio:contact_submit'),
            data=json.dumps(post_data),
            content_type='application/json',
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['status'], 'success')

        # Verify record in database
        msg = ContactMessage.objects.filter(email='client@example.com').first()
        self.assertIsNotNone(msg)
        self.assertEqual(msg.name, 'Client User')
        self.assertEqual(msg.subject, 'Project Consultation')

    def test_api_project_detail(self):
        url = reverse('portfolio:project_detail_api', kwargs={'project_id': self.project.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['status'], 'success')
        self.assertEqual(data['project']['title'], 'Test Project')
        self.assertIn('Django', data['project']['tech_stack'])
