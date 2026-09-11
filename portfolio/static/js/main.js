/**
 * Personal Portfolio - Interactive Client Logic
 * Handles filtering, modal details, AJAX contact submissions, and animations.
 */

document.addEventListener('DOMContentLoaded', () => {
    initNavigation();
    initProjectFiltering();
    initProjectModal();
    initContactForm();
    initScrollAnimations();
    initStatsCounter();
});

/* ==================== NAVIGATION ==================== */
function initNavigation() {
    const mobileToggle = document.getElementById('mobile-toggle');
    const navMenu = document.getElementById('nav-menu');
    const navLinks = document.querySelectorAll('.nav-link');

    if (mobileToggle && navMenu) {
        mobileToggle.addEventListener('click', () => {
            navMenu.classList.toggle('active');
            const icon = mobileToggle.querySelector('i');
            if (icon) {
                icon.classList.toggle('fa-bars');
                icon.classList.toggle('fa-xmark');
            }
        });

        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                navMenu.classList.remove('active');
                const icon = mobileToggle.querySelector('i');
                if (icon) {
                    icon.classList.add('fa-bars');
                    icon.classList.remove('fa-xmark');
                }
            });
        });
    }

    // Header scroll background styling
    const header = document.getElementById('navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.style.background = 'rgba(10, 14, 23, 0.95)';
            header.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.4)';
        } else {
            header.style.background = 'rgba(10, 14, 23, 0.85)';
            header.style.boxShadow = 'none';
        }
    });
}

/* ==================== PROJECT FILTERING ==================== */
function initProjectFiltering() {
    const filterBtns = document.querySelectorAll('.filter-btn');
    const projectCards = document.querySelectorAll('.project-card');

    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            filterBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const filterValue = btn.getAttribute('data-filter');

            projectCards.forEach(card => {
                const category = card.getAttribute('data-category');
                if (filterValue === 'all' || category === filterValue) {
                    card.style.display = 'flex';
                    setTimeout(() => {
                        card.style.opacity = '1';
                        card.style.transform = 'translateY(0)';
                    }, 50);
                } else {
                    card.style.opacity = '0';
                    card.style.transform = 'translateY(15px)';
                    setTimeout(() => {
                        card.style.display = 'none';
                    }, 250);
                }
            });
        });
    });
}

/* ==================== PROJECT MODAL ==================== */
function initProjectModal() {
    const modal = document.getElementById('project-modal');
    const modalBody = document.getElementById('modal-body');
    const modalClose = document.getElementById('modal-close');
    const detailButtons = document.querySelectorAll('.btn-detail');

    if (!modal || !modalBody) return;

    detailButtons.forEach(btn => {
        btn.addEventListener('click', async (e) => {
            e.preventDefault();
            const projectId = btn.getAttribute('data-project-id');
            if (!projectId) return;

            // Open modal in loading state
            modal.classList.add('active');
            modalBody.innerHTML = `
                <div style="text-align: center; padding: 40px;">
                    <i class="fa-solid fa-spinner fa-spin" style="font-size: 2rem; color: #06B6D4;"></i>
                    <p style="margin-top: 16px; color: #94A3B8;">Loading project details...</p>
                </div>
            `;

            try {
                const response = await fetch(`/api/projects/${projectId}/`);
                if (!response.ok) throw new Error('Failed to load project details');
                const data = await response.json();

                if (data.status === 'success' && data.project) {
                    const p = data.project;
                    const techPills = p.tech_stack.map(t => `<span class="tech-tag">${t}</span>`).join(' ');
                    
                    modalBody.innerHTML = `
                        <img src="${p.image_url}" alt="${p.title}" class="modal-img">
                        <div class="project-category-badge" style="position: static; display: inline-block; margin-bottom: 12px;">${p.category}</div>
                        <h2 class="modal-title">${p.title}</h2>
                        <div class="modal-meta">
                            <span><i class="fa-regular fa-calendar"></i> Added in ${p.created_at}</span>
                        </div>
                        <p class="modal-desc">${p.full_description}</p>
                        <h4 style="margin-bottom: 10px; font-size: 0.95rem; color: #F9FAFB;">Technologies & Architecture:</h4>
                        <div class="tech-tags" style="margin-bottom: 24px;">
                            ${techPills}
                        </div>
                        <div class="modal-actions">
                            ${p.github_url && p.github_url !== '#' ? `
                                <a href="${p.github_url}" target="_blank" rel="noopener" class="btn btn-outline">
                                    <i class="fa-brands fa-github"></i> View GitHub Code
                                </a>
                            ` : ''}
                            ${p.live_demo_url && p.live_demo_url !== '#' ? `
                                <a href="${p.live_demo_url}" target="_blank" rel="noopener" class="btn btn-primary">
                                    <i class="fa-solid fa-arrow-up-right-from-square"></i> Open Live App
                                </a>
                            ` : ''}
                            ${(!p.github_url || p.github_url === '#') && (!p.live_demo_url || p.live_demo_url === '#') ? `
                                <span style="display:inline-flex; align-items:center; gap:8px; background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.1); padding:8px 18px; border-radius:9999px; font-size:0.85rem; color:#94A3B8;">
                                    <i class="fa-solid fa-lock"></i> Internal Project / Repository Private
                                </span>
                            ` : ''}
                        </div>
                    `;
                } else {
                    modalBody.innerHTML = `<p style="color: #EF4444; padding: 20px;">Could not retrieve project information.</p>`;
                }
            } catch (err) {
                console.error(err);
                modalBody.innerHTML = `<p style="color: #EF4444; padding: 20px;">Error connecting to backend service.</p>`;
            }
        });
    });

    const closeModal = () => {
        modal.classList.remove('active');
    };

    if (modalClose) {
        modalClose.addEventListener('click', closeModal);
    }

    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            closeModal();
        }
    });

    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && modal.classList.contains('active')) {
            closeModal();
        }
    });
}

/* ==================== CONTACT FORM AJAX ==================== */
function initContactForm() {
    const form = document.getElementById('contact-form');
    if (!form) return;

    const submitBtn = document.getElementById('contact-submit-btn');
    const btnText = submitBtn ? submitBtn.querySelector('.btn-text') : null;
    const spinner = submitBtn ? submitBtn.querySelector('.spinner-inline') : null;

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const name = form.querySelector('[name="name"]').value.trim();
        const email = form.querySelector('[name="email"]').value.trim();
        const subject = form.querySelector('[name="subject"]').value.trim();
        const message = form.querySelector('[name="message"]').value.trim();

        if (!name || !email || !message) {
            showToast('Please fill in all required fields.', 'error');
            return;
        }

        // Set Loading State
        if (submitBtn) submitBtn.disabled = true;
        if (btnText) btnText.classList.add('hidden');
        if (spinner) spinner.classList.remove('hidden');

        // Extract CSRF Token
        const csrfToken = form.querySelector('[name="csrfmiddlewaretoken"]')?.value;

        try {
            const response = await fetch(form.action, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken,
                    'X-Requested-With': 'XMLHttpRequest'
                },
                body: JSON.stringify({ name, email, subject, message })
            });

            const result = await response.json();

            if (response.ok && result.status === 'success') {
                showToast(result.message || 'Your message has been sent successfully!', 'success');
                form.reset();
            } else {
                showToast(result.message || 'Failed to send message. Please try again.', 'error');
            }
        } catch (error) {
            console.error('Contact submission error:', error);
            showToast('Unable to send message. Please try again later.', 'error');
        } finally {
            if (submitBtn) submitBtn.disabled = false;
            if (btnText) btnText.classList.remove('hidden');
            if (spinner) spinner.classList.add('hidden');
        }
    });
}

/* ==================== TOAST NOTIFICATION HELPER ==================== */
function showToast(message, type = 'success') {
    const container = document.getElementById('toast-container');
    if (!container) return;

    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;
    
    const iconClass = type === 'success' ? 'fa-solid fa-circle-check' : 'fa-solid fa-circle-exclamation';
    toast.innerHTML = `<i class="${iconClass}"></i> <span>${message}</span>`;

    container.appendChild(toast);

    setTimeout(() => {
        toast.style.opacity = '0';
        toast.style.transform = 'translateX(100%)';
        toast.style.transition = 'all 0.3s ease';
        setTimeout(() => toast.remove(), 300);
    }, 4500);
}

/* ==================== SCROLL ANIMATIONS ==================== */
function initScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('in-view');
            }
        });
    }, observerOptions);

    document.querySelectorAll('.skill-category-card, .project-card, .timeline-item').forEach(el => {
        observer.observe(el);
    });
}

/* ==================== STATS COUNTER ==================== */
function initStatsCounter() {
    const statCards = document.querySelectorAll('.stat-number[data-count]');
    let hasAnimated = false;

    const statsObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !hasAnimated) {
                hasAnimated = true;
                statCards.forEach(stat => {
                    const target = parseInt(stat.getAttribute('data-count'), 10);
                    if (isNaN(target)) return;

                    let current = 0;
                    const increment = Math.max(1, Math.ceil(target / 30));
                    const timer = setInterval(() => {
                        current += increment;
                        if (current >= target) {
                            stat.textContent = `${target}+`;
                            clearInterval(timer);
                        } else {
                            stat.textContent = `${current}+`;
                        }
                    }, 40);
                });
            }
        });
    }, { threshold: 0.3 });

    const statsSection = document.querySelector('.stats-section');
    if (statsSection) {
        statsObserver.observe(statsSection);
    }
}
