from django.contrib import admin
from django.urls import path, include
import movie_app.views as movie_views
from . import swagger
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/movies/', movie_views.MoviesListAPIView.as_view()),
    path('api/v1/movies/reviews/', movie_views.MovieReviewsListAPIView.as_view()),
    path('api/v1/movies/<int:id>/', movie_views.MovieItemUpdateDeleteAPIView.as_view()),
    path('api/v1/directors/', movie_views.DirectorListAPIView.as_view()),
    path('api/v1/directors/<int:id>/', movie_views.DirectorItemUpdateDeleteAPIView.as_view()),
    path('api/v1/reviews/', movie_views.ReviewModelViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('api/v1/reviews/<int:id>/', movie_views.ReviewModelViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('api/v1/users/', include('users.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += swagger.urlpatterns
