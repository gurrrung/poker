from django.urls import path, include

from django.views.generic import TemplateView

urlpatterns = [
  path('', TemplateView.as_view(template_name="cron/index.html")),
  path('', include('cron.views.pages.urls')),
  path('api/', include('cron.views.api.urls'))
]
