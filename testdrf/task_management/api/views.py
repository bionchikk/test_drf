from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import User, Task
from .serializers import UserSerializer, TaskSerializer
from .permissions import IsEmployeeOrReadOnly, IsClientOrReadOnly

class UserDetailView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_employee:
            return Task.objects.all()
        return Task.objects.filter(client=user)

class TaskDetailView(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsEmployeeOrReadOnly, IsClientOrReadOnly]

    def perform_update(self, serializer):
        if self.get_object().status == 'completed':
            raise serializers.ValidationError('Выполненную задачу редактировать нельзя.')
        serializer.save()
