-- =============================================================================
-- Initial Data Population Script for ShriramPortfolio
-- Target Host: 34.100.184.249
-- Database: Portfoliodb
-- =============================================================================

USE `Portfoliodb`;

-- 1. Insert Profile for Shriram S
INSERT INTO `portfolio_profile` (
    `id`, `full_name`, `tagline`, `bio`, `about_details`,
    `years_of_experience`, `completed_projects_count`, `happy_clients_count`,
    `location`, `email`, `phone`, `github_url`, `linkedin_url`, `twitter_url`,
    `resume_url`, `avatar_url`, `is_active`, `updated_at`
) VALUES (
    1,
    'Shriram S',
    'Python & Cloud Developer | Unity Game Dev & Responsive Web | Intern at Thiranex',
    'Enthusiastic and versatile developer well versed with Python and Cloud Computing, experienced in Ecommerce Responsive Web Design and Unity Game Development. Currently interning at Thiranex while pursuing CSE at Easwari Engineering College and a BS Degree at IIT Madras.',
    'I am a passionate, multidisciplinary developer specializing in Python engineering, scalable Cloud Computing, modern Ecommerce responsive web design, and interactive Unity Game Development with C#. Currently working as an intern at Thiranex, I turn complex technical specifications into performant, elegant digital solutions. Having completed high school at Apex Pon Vidyashram, I am currently expanding my foundations through dual academic programs: Computer Science Engineering at Easwari Engineering College and the esteemed BS Degree program at IIT Madras.',
    2, 14, 10,
    'Chennai, India',
    's.shriramsivakumaran@gmail.com',
    '9994949819',
    'https://github.com/StarShree',
    'https://www.linkedin.com/in/shriramsss/',
    'https://twitter.com',
    '#contact',
    '',
    1,
    NOW(6)
) ON DUPLICATE KEY UPDATE 
    `full_name`=VALUES(`full_name`),
    `tagline`=VALUES(`tagline`),
    `bio`=VALUES(`bio`),
    `about_details`=VALUES(`about_details`),
    `email`=VALUES(`email`),
    `phone`=VALUES(`phone`),
    `github_url`=VALUES(`github_url`),
    `linkedin_url`=VALUES(`linkedin_url`);

-- 2. Insert Skill Categories
INSERT INTO `portfolio_skillcategory` (`id`, `name`, `icon`, `order`) VALUES
(1, 'Python & Backend Engineering', 'server', 1),
(2, 'Cloud Computing & DevOps', 'cloud', 2),
(3, 'Unity Game Development', 'gamepad', 3),
(4, 'Frontend & Ecommerce Web Design', 'layout', 4),
(5, 'Databases & Data Systems', 'database', 5)
ON DUPLICATE KEY UPDATE `name`=VALUES(`name`);

-- 3. Insert Skills
INSERT INTO `portfolio_skill` (`id`, `category_id`, `name`, `proficiency`, `icon_class`, `is_featured`, `order`) VALUES
(1, 1, 'Python (Core, OOP, Scripting)', 95, 'fa-brands fa-python', 1, 1),
(2, 1, 'Django & Django REST Framework', 90, 'fa-brands fa-python', 1, 2),
(3, 1, 'RESTful API Design & Integration', 88, 'fa-solid fa-network-wired', 1, 3),
(4, 1, 'Data Structures & Algorithmic Problem Solving', 85, 'fa-solid fa-code', 0, 4),

(5, 2, 'Cloud Computing Architecture & Principles', 92, 'fa-solid fa-cloud', 1, 1),
(6, 2, 'Google Cloud Platform & Cloud Services', 88, 'fa-brands fa-google', 1, 2),
(7, 2, 'Docker & Containerized Microservices', 84, 'fa-brands fa-docker', 1, 3),
(8, 2, 'Git & GitHub Version Control Workflows', 95, 'fa-brands fa-github', 1, 4),

(9, 3, 'Unity Engine (2D & 3D Game Design)', 88, 'fa-solid fa-gamepad', 1, 1),
(10, 3, 'C# Gameplay Scripting & State Machines', 86, 'fa-solid fa-code', 1, 2),
(11, 3, 'Game Physics, Colliders & Raycasting', 84, 'fa-solid fa-cube', 1, 3),
(12, 3, 'Animation Controllers & Asset Integration', 82, 'fa-solid fa-film', 0, 4),

(13, 4, 'Ecommerce Website Responsive Design', 94, 'fa-solid fa-bag-shopping', 1, 1),
(14, 4, 'Modern CSS3 (Flexbox, Grid, Glassmorphism)', 92, 'fa-brands fa-css3-alt', 1, 2),
(15, 4, 'HTML5 Semantic Architecture & Accessibility', 95, 'fa-brands fa-html5', 1, 3),
(16, 4, 'JavaScript (ES6+) & Asynchronous DOM', 88, 'fa-brands fa-js', 0, 4),

(17, 5, 'MySQL & Relational Data Modeling', 90, 'fa-solid fa-database', 1, 1),
(18, 5, 'SQL Query Optimization & Indexing', 86, 'fa-solid fa-bolt', 1, 2),
(19, 5, 'Database Migrations & ORM Abstraction', 88, 'fa-solid fa-diagram-project', 0, 3)
ON DUPLICATE KEY UPDATE `proficiency`=VALUES(`proficiency`);

-- 4. Insert Projects (including Ecommerce & Unity Game Dev with no links)
INSERT INTO `portfolio_project` (
    `id`, `title`, `slug`, `category`, `short_description`, `full_description`,
    `tech_stack`, `image_url`, `live_demo_url`, `github_url`, `is_featured`, `order`, `created_at`
) VALUES
(
    1,
    'Ecommerce Website Responsive Design',
    'ecommerce-website-responsive-design',
    'fullstack',
    'Full-featured, mobile-first responsive ecommerce web platform with dynamic catalogs and cart mechanics.',
    'Engineered a responsive ecommerce web storefront designed to deliver exceptional user experiences across mobile, tablet, and desktop viewports. Implemented optimized product showcase grids, dynamic filtering, intuitive cart interactions, and clean semantic structure following modern UI/UX design standards.',
    'HTML5, CSS3, JavaScript, Responsive Design, Python',
    'https://images.unsplash.com/photo-1522542550221-31fd19575a2d?auto=format&fit=crop&w=800&q=80',
    '#',
    '#',
    1, 1, NOW(6)
),
(
    2,
    'Unity Game Dev',
    'unity-game-dev-project',
    'gamedev',
    'Interactive 2D/3D game development project engineered in Unity with C#, custom physics, and gameplay loops.',
    'Designed and developed an engaging game experience inside the Unity Engine using C#. Incorporates custom player movement controllers, collision and physics systems, enemy AI behaviors, interactive environment triggers, sound design integration, and dynamic level progression.',
    'Unity Engine, C#, Game Physics, 2D/3D Animation, Asset Design',
    'https://images.unsplash.com/photo-1550745165-9bc0b252726f?auto=format&fit=crop&w=800&q=80',
    '#',
    '#',
    1, 2, NOW(6)
),
(
    3,
    'Cloud Computing Automated Telemetry & Monitor',
    'cloud-computing-telemetry-monitor',
    'cloud',
    'Automated server health and cloud service monitoring tool built with Python.',
    'Developed automated monitoring scripts that track uptime, request latency, and memory footprints across cloud instances. Built as part of cloud computing explorations with asynchronous alert dispatching.',
    'Python, Cloud Infrastructure, Docker, Linux, Shell Scripting',
    'https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800&q=80',
    '#',
    'https://github.com/StarShree',
    1, 3, NOW(6)
),
(
    4,
    'Python High-Throughput RESTful API Service',
    'python-throughput-rest-api',
    'backend',
    'Performant backend web service implementing secure token authentication, caching, and rate-limiting.',
    'Engineered a scalable RESTful API with Django and Python. Features automated input validation, relational database indexing, and clean layered service architecture.',
    'Python, Django REST, SQL, JSON, Postman',
    'https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=800&q=80',
    '#',
    'https://github.com/StarShree',
    1, 4, NOW(6)
),
(
    5,
    'Cloud-Native Personal Portfolio & Showcase Engine',
    'shriram-portfolio-engine',
    'fullstack',
    'Full-stack personal portfolio system engineered with Django backend, cloud database, and dynamic glassmorphic UI.',
    'Designed and deployed a responsive personal portfolio featuring dynamic project showcase, AJAX contact handling, administrative control panels, and cloud data persistence. Built with clean architecture principles.',
    'Python, Django, Cloud Database, JavaScript, CSS3',
    'https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=80',
    '#',
    'https://github.com/StarShree',
    1, 5, NOW(6)
)
ON DUPLICATE KEY UPDATE `title`=VALUES(`title`);

-- 5. Insert Experience
INSERT INTO `portfolio_experience` (
    `id`, `role`, `company`, `location`, `start_date`, `end_date`, `description`, `technologies`, `order`
) VALUES
(
    1,
    'Software Development & Cloud Intern',
    'Thiranex',
    'Chennai / Remote',
    '2024',
    'Present',
    'Actively engaged in software engineering workflows, backend development with Python, and cloud computing initiatives. Collaborating on core features, optimizing application performance, and maintaining robust codebase standards.',
    'Python, Cloud Computing, Django, MySQL, Git, Linux',
    1
),
(
    2,
    'Python, Cloud & Game Development Specialist',
    'Technical Projects & Academic Initiatives',
    'Chennai, India',
    '2023',
    'Present',
    'Well versed in Python development, scalable cloud architectures, responsive web design for ecommerce applications, and interactive 2D/3D game design using the Unity Engine and C#.',
    'Python, Cloud Computing, Unity, C#, HTML5/CSS3, MySQL, Git',
    2
)
ON DUPLICATE KEY UPDATE `role`=VALUES(`role`);

-- 6. Insert Education (Apex Pon Vidyashram, Easwari Engineering College, IITM BS Degree)
INSERT INTO `portfolio_education` (
    `id`, `degree`, `institution`, `period`, `grade_or_details`, `order`
) VALUES
(
    1,
    'B.E. in Computer Science and Engineering (CSE)',
    'Easwari Engineering College',
    'Currently Enrolled',
    'Pursuing core Computer Science curriculum including Operating Systems, DBMS, Algorithms, and Cloud Systems.',
    1
),
(
    2,
    'BS Degree in Data Science & Applications',
    'IIT Madras (IITM)',
    'Currently Enrolled',
    'Premier degree program by IITM covering Python programming, mathematical foundations, data science, and modern computation.',
    2
),
(
    3,
    'High School Education',
    'Apex Pon Vidyashram',
    'Finished / Graduated',
    'Completed High School education with rigorous preparation in Computer Science, Mathematics, and Sciences.',
    3
)
ON DUPLICATE KEY UPDATE `degree`=VALUES(`degree`);
