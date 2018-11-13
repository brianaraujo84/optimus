from django.contrib import admin
from django.urls import include, path
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view 
from rest_framework_swagger.views import get_swagger_view

API_TITLE = 'PROYECTO SEGURIDAD DE LA INFORMACION' 
API_DESCRIPTION = 'A Web API for creating and editing PROY SEG INFO'
schema_view = get_swagger_view(title=API_TITLE)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
    path('auth/', include('rest_framework.urls')),
    path('auth/rest-auth/', include('rest_auth.urls')),
    path('auth/rest-auth/registration/', include('rest_auth.registration.urls')),
    path('docs/', include_docs_urls(title=API_TITLE,     
                                    description=API_DESCRIPTION)),
    # path('schema/', schema_view), 
    path('swagger-docs/', schema_view),
]