from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.db import connection
import json

from .models import (
    Profile,
    SkillCategory,
    Skill,
    Project,
    Experience,
    Education,
    ContactMessage,
)


def index(request):
    """Render the main single-page portfolio with dynamic data from Google Cloud SQL."""
    profile = Profile.objects.filter(is_active=True).first()
    if not profile:
        # Fallback profile if none has been created yet
        profile = Profile()

    categories = SkillCategory.objects.prefetch_related('skills').all()
    projects = Project.objects.all()
    experiences = Experience.objects.all()
    educations = Education.objects.all()

    # Determine unique categories present in projects
    project_categories = sorted(list(set(projects.values_list('category', flat=True))))

    # Database connectivity verification info
    db_connected = False
    db_name = "Portfoliodb"
    db_host = "34.100.184.249"
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1;")
            db_connected = True
    except Exception:
        db_connected = False

    context = {
        'profile': profile,
        'categories': categories,
        'projects': projects,
        'project_categories': project_categories,
        'experiences': experiences,
        'educations': educations,
        'db_connected': db_connected,
        'db_name': db_name,
        'db_host': db_host,
    }
    return render(request, 'portfolio/index.html', context)


@csrf_exempt
@require_POST
def contact_submit(request):
    """Handle contact form submissions, storing message in Cloud SQL MySQL."""
    is_ajax = (
        request.headers.get('x-requested-with') == 'XMLHttpRequest'
        or request.content_type == 'application/json'
    )

    name = ""
    email = ""
    subject = ""
    message_text = ""

    if request.content_type == 'application/json':
        try:
            data = json.loads(request.body)
            name = data.get('name', '').strip()
            email = data.get('email', '').strip()
            subject = data.get('subject', '').strip()
            message_text = data.get('message', '').strip()
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON data.'}, status=400)
    else:
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message_text = request.POST.get('message', '').strip()

    if not name or not email or not message_text:
        msg = "Please fill in all required fields (Name, Email, Message)."
        if is_ajax:
            return JsonResponse({'status': 'error', 'message': msg}, status=400)
        messages.error(request, msg)
        return redirect('portfolio:index')

    # Save to MySQL Database
    contact_obj = ContactMessage.objects.create(
        name=name,
        email=email,
        subject=subject or f"Portfolio Inquiry from {name}",
        message=message_text,
    )

    success_msg = f"Thank you, {name}! Your message has been received and I will get back to you shortly."
    if is_ajax:
        return JsonResponse({
            'status': 'success',
            'message': success_msg,
            'id': contact_obj.id,
        })

    messages.success(request, success_msg)
    return redirect('portfolio:index')


def api_project_detail(request, project_id):
    """Return JSON details for a specific project to display in modal."""
    project = get_object_or_404(Project, id=project_id)
    data = {
        'id': project.id,
        'title': project.title,
        'category': project.get_category_display(),
        'short_description': project.short_description,
        'full_description': project.full_description,
        'tech_stack': project.tech_list,
        'image_url': project.image_url,
        'live_demo_url': project.live_demo_url,
        'github_url': project.github_url,
        'created_at': project.created_at.strftime('%B %Y'),
    }
    return JsonResponse({'status': 'success', 'project': data})
