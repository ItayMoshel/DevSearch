from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from projects.models import Project
from users.models import User, Message, Test
from .serializers import ProjectSerializer, ProfileSerializer, MessageSerializer, TestSerializer



@api_view(['GET'])
def getRoutes(request):
    
    routes = [
        {'GET':'/api/projects'},
        {'GET':'/api/projects/id'},
        {'POST':'/api/projects/id/vote'},
        
        {'POST':'/api/users/token'},
        {'POST':'/api/users/token/refresh'},
        
    ]
    return Response(routes)


@api_view(['GET'])
def getProjects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProject(request, pk):
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getProfiles(request):
    users = User.objects.all()
    serializer = ProfileSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProfile(request, pk):
    user = User.objects.get(id=pk)
    serializer = ProfileSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getMessages(request):
    messages = Message.objects.all()
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createTest(request):
    t = TestSerializer(data=request.data)
    if t.is_valid():
        t.save()
        return Response(t.data)
    return Response(t.errors)
    
    
@api_view(['POST'])
def createMessage(request):
    t = MessageSerializer(data=request.data)
    print(request.data)
    if t.is_valid():
        t.save()
        return Response(t.data)
    return Response(t.errors)
