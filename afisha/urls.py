from django.contrib import admin
from django.urls import path, include
import movie_app.views as movie_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/directors/', movie_views.directors_view),
    path('api/v1/movies/', movie_views.movies_view),
    path('api/v1/reviews/', movie_views.reviews_view),
    path('api/v1/movies/reviews/', movie_views.movie_reviews_view),
    path('api/v1/movies/<int:id>/', movie_views.movie_item_view),
    path('api/v1/directors/<int:id>/', movie_views.director_item_view),
    path('api/v1/reviews/<int:id>/', movie_views.review_item_view),
    path('api/v1/users/', include('users.urls'))
]
