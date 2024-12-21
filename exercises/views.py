from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from accounts.permissions import IsAdminOrTrainerPermission
from .models import Exercise
from .serializers import ExerciseSerializer
from .models import ExerciseCategory
from .serializers import ExerciseCategorySerializer
from .models import ExerciseType
from .serializers import ExerciseTypeSerializer

class ExercisePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'limit'


class ExerciseListView(generics.ListAPIView):
    serializer_class = ExerciseSerializer

    def get_queryset(self):
        category_id = self.request.query_params.get('category', None)
        exercise_type_id = self.request.query_params.get('exercise_type', None)

        queryset = Exercise.objects.all()

        if category_id:
            queryset = queryset.filter(category_id=category_id)

        if exercise_type_id:
            queryset = queryset.filter(exercise_type_id=exercise_type_id)

        return queryset


class ExerciseCreateView(generics.ListCreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [IsAuthenticated, IsAdminOrTrainerPermission]



class ExerciseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [IsAuthenticated, IsAdminOrTrainerPermission]





class ExerciseCategoryListView(generics.ListAPIView):
    queryset = ExerciseCategory.objects.all()
    serializer_class = ExerciseCategorySerializer
    pagination_class = ExercisePagination
    # permission_classes = [IsAuthenticated]
    authentication_classes = []
    permission_classes = []


class ExerciseCategoryListCreateView(generics.ListCreateAPIView):
    queryset = ExerciseCategory.objects.all()
    serializer_class = ExerciseCategorySerializer
    permission_classes = [IsAuthenticated, IsAdminOrTrainerPermission]


class ExerciseCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExerciseCategory.objects.all()
    serializer_class = ExerciseCategorySerializer


class ExerciseTypeListView(generics.ListAPIView):
    queryset = ExerciseType.objects.all()
    serializer_class = ExerciseTypeSerializer
    pagination_class = ExercisePagination
    # permission_classes = [IsAuthenticated]
    authentication_classes = []
    permission_classes = []

class ExerciseTypeListCreateView(generics.ListCreateAPIView):
    queryset = ExerciseType.objects.all()
    serializer_class = ExerciseTypeSerializer
    permission_classes = [IsAuthenticated, IsAdminOrTrainerPermission]


class ExerciseTypeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExerciseType.objects.all()
    serializer_class = ExerciseTypeSerializer
