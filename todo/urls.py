from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, TaskCategoryViewSet, TaskViewSet, UserViewSet
from rest_framework.authtoken import views


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'task', TaskViewSet,basename="task")
router.register(r'task-category', TaskCategoryViewSet,basename="tc")
router.register(r'user', UserViewSet, basename='user' )
router.register(r'category', CategoryViewSet, basename='category')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('api/', include(router.urls)),
    
]

urlpatterns += [
    path('api-token-auth/', views.obtain_auth_token),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken'))
]

