from django.urls import path
from .views import (
    ExerciseDetailView,
    ExerciseCategoryDetailView,
    ExerciseTypeListCreateView, ExerciseTypeDetailView, ExerciseListView, ExerciseCreateView, ExerciseCategoryListView,
    ExerciseTypeListView
)

urlpatterns = [

    path('exercises/', ExerciseListView.as_view(), name='exercise_list'),
    path('exercises/create/', ExerciseCreateView.as_view(), name='exercise_create'),
    path('exercises/<int:pk>/', ExerciseDetailView.as_view(), name='exercise_detail'),


    path('categories/', ExerciseCategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/', ExerciseCategoryDetailView.as_view(), name='category_detail'),


    path('types/', ExerciseTypeListView.as_view(), name='type_create'),
    path('types/<int:pk>/', ExerciseTypeDetailView.as_view(), name='type_detail'),
]
