# MyBlog (Django)

MyBlog is a Django-based blogging application featuring posts, categories, tags, comments with moderation, contact form with captcha, and a simple authentication system. The project uses a clean design system powered by CSS variables and consistent templates.

## Features
- Blog home with pagination
- Single post page with views count
- Categories and tags filtering
- Comment system with moderation (admin approval required before display)
- Contact form with captcha protection
- Authentication: register, login, logout
- Latest posts and recent comments widgets via Django template tags
- Media uploads for post images

## Tech Stack
- Django 6.x
- Python 3.11+ (works with 3.13)
- SQLite (default) — easy local dev
- django-simple-captcha (for captcha)
- Pillow (for ImageField)

## Project Structure
```
myblog/                  # Django project (settings/urls/wsgi)
accounts/                # Custom user model and auth views
posts/                   # Blog app: models, views, urls, template tags
templates/
  base.html              # Global layout
  blog/                  # New blog namespace templates
    blog.html            # Blog listing page
    single.html          # Single post page
    comment.html         # Comments block
    partials/sidebar/    # Sidebar widgets
      latest_posts.html
      recent_comments.html
      categories.html
      tag_cloud.html
      search.html
media/                   # Uploaded images (e.g., blog_images/)
manage.py                # Django entry point
```

## Installation

### Prerequisites
- Python 3.11+
- pip

### 1) Clone the repository
```bash
git clone <your-repo-url> && cd blog
```

### 2) Create and activate a virtual environment
```bash
python -m venv .venv
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
# macOS/Linux
source .venv/bin/activate
```

### 3) Install dependencies
If you have a requirements file:
```bash
pip install -r requirements.txt
```
Alternatively, install packages directly:
```bash
pip install "Django>=6,<7" django-simple-captcha Pillow
```

### 4) Database migrations
```bash
python manage.py migrate
```

### 5) Create a superuser (for admin and comment moderation)
```bash
python manage.py createsuperuser
```

### 6) Run the development server
```bash
python manage.py runserver
```
Then open http://127.0.0.1:8000/ in your browser.

## Configuration

### Settings
- Project settings live in [myblog/settings.py](file:///g:/Python/Django/blog/myblog/settings.py).
- Authentication user model: `AUTH_USER_MODEL = 'accounts.CustomUser'`.
- Media uploads: `MEDIA_URL = '/media/'`, `MEDIA_ROOT = BASE_DIR / 'media'`.

### URLs
- Root URLConf: [myblog/urls.py](file:///g:/Python/Django/blog/myblog/urls.py)
- Blog app URLs: [posts/urls.py](file:///g:/Python/Django/blog/posts/urls.py)

The blog is exposed under the `blog` namespace. Ensure your root URLConf includes the blog namespace when including the app’s URLs:
```python
# myblog/urls.py
from django.urls import include, path
urlpatterns = [
    path('admin/', admin.site.urls),
    # Namespace the blog
    path('', include(('posts.urls', 'blog'), namespace='blog')),
    path('accounts/', include('accounts.urls')),
    path('captcha/', include('captcha.urls')),
]
```

## Usage and Pages

### Blog
- Home (paginated): `/`
- Single post: `/<post-id>/` (e.g., `/5/`)
- Search: `/search/?s=<query>`
- Filter by category: `/category/<slug>`
- Filter by tag: `/tag/<slug>/`

Templates:
- Listing: [blog.html](file:///g:/Python/Django/blog/templates/blog/blog.html)
- Single: [single.html](file:///g:/Python/Django/blog/templates/blog/single.html)
- Comments: [comment.html](file:///g:/Python/Django/blog/templates/blog/comment.html)

### Comments
- Users must be authenticated to post comments.
- Comments default to `is_active=False`, and are shown only after admin approval.
- Approve comments via Django admin.

### Contact
- Contact form is backed by `ContactMessage` and uses captcha.
- View: [posts/views.py:contact](file:///g:/Python/Django/blog/posts/views.py#L99-L110)
- Template: [templates/contact.html](file:///g:/Python/Django/blog/templates/contact.html)

Important: If you keep a raw HTML contact template, ensure captcha fields are rendered and posted. Otherwise, remove captcha from the form or convert the template to render `{{ form.captcha }}` fields.

### Authentication (accounts)
- Register: `/accounts/register/`
- Login: `/accounts/login/`
- Logout: `/accounts/logout/`

URLs: [accounts/urls.py](file:///g:/Python/Django/blog/accounts/urls.py)

`CustomUser` model fields include username, email, phone_number, first_name, last_name, and biography. Registration template matches these fields.

## Admin
- Access admin at `/admin/`.
- Moderate comments (set `is_active=True` to publish).
- Manage posts, categories, and tags.

## Media
- Post images stored in `media/blog_images/`.
- Ensure `MEDIA_URL` and `MEDIA_ROOT` are configured, and serve media in dev:
```python
# myblog/urls.py (already present)
from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

<<<<<<< HEAD
## Development Tips
- Template tags are in [posts/templatetags/blog_tags.py](file:///g:/Python/Django/blog/posts/templatetags/blog_tags.py).
- Uses a consistent design system via CSS variables in [base.html](file:///g:/Python/Django/blog/templates/base.html).
- Pagination, widgets, and layout are unified across blog pages.

## Testing
Run Django tests:
```bash
python manage.py test
```
=======
>>>>>>> bd11ced6a909f2ac200bfb2fb2fbcd1f31cb999a

## Deployment Notes
- Set `DEBUG = False` and configure `ALLOWED_HOSTS` in production.
- Generate a strong `SECRET_KEY` for production environment.
- Configure a production-grade database (PostgreSQL, MySQL, etc.) as needed.
- Configure static files (STATIC_ROOT) and collectstatic.

<<<<<<< HEAD
## Troubleshooting
- Namespaced URLs: If you see `NoReverseMatch` errors for `blog:*`, ensure `myblog/urls.py` includes `namespace='blog'` when including `posts.urls` (see Configuration section).
- Contact form captcha: If submissions always fail, include captcha fields in the template or remove the captcha field from `ContactForm`.
- Comments not visible: Approve comments in admin or change default to `is_active=True` if immediate display is desired.

## License
Add your chosen license here (MIT, Apache-2.0, etc.).

## Acknowledgements
- Django community and documentation
- django-simple-captcha
- Google Fonts (Inter)
=======
## License
MIT License
>>>>>>> bd11ced6a909f2ac200bfb2fb2fbcd1f31cb999a
