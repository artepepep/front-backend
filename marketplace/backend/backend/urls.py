from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi

# schema_view = get_schema_view(
#     openapi.Info(
#         title="TeamChallenge",
#         default_version='v1',
#         description="API for Sviy marketplace",
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('simple-auth/', include('djoser.urls')), # вся система регистрации
    path('api/v1/drf-auth/', include('rest_framework.urls')), # для логина и логаута обычного
    path('products/', include('productsapi.urls')),
    path('custom-users/', include('users.urls')),
	path("authentication-by-google/", include("authentication.urls")),
	path("all-payments/", include("payment.urls")),
	path("__debug__/", include("debug_toolbar.urls")),
    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
	re_path(r'^jwt-auth/', include('djoser.urls.jwt')),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
