




from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter

from account.models import Account
from event.api.serializers import EventPostCreateSerializer,EventPostSerializer
from event.models import EventPost
from event.api.utils import is_time_between


@api_view(['POST',])
@permission_classes((IsAuthenticated,))
def api_event_create_view(request):
    if request.method == "POST":
        data = request.data
        user = Account.objects.get(email = request.user.email)
        organizer = user
        serializer = EventPostCreateSerializer(data = data)
        data = {}
        if serializer.is_valid(request.data):
            event = serializer.save(request.data)
            event.organizer = organizer
            event.save()
            data['success']=True
        else:
            data['failed']=True
        return Response(data)
        

# # Headers: Authorization: Token <token>
@api_view(['DELETE',])
@permission_classes((IsAuthenticated, ))
def api_delete_event_view(request, slug):

	try:
		event_post = EventPost.objects.get(slug=slug)
	except EventPost.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	user = request.user
	if event_post.organizer != user:
		return Response({'response':"You don't have permission to delete that."}) 

	if request.method == 'DELETE':
		operation = event_post.delete()
		data = {}
		if operation:
			data['response'] = 'DELETE_SUCCESS'
		return Response(data=data)


@api_view(['GET',])
def api_event_detail_slug_view(request,slug):
    try:
        event_post = EventPost.objects.get(slug=slug)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    serializer = EventPostSerializer(event_post)
    return Response(serializer.data)





@api_view(['POST',])
@permission_classes((IsAuthenticated, ))
def api_event_invite_view(request, slug):
    try:
        event_post = EventPost.objects.get(slug=slug)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    user = request.user
    if event_post.organizer != user:
        return Response({'response':"You don't have permission to delete that."})

    if request.method == 'POST':
        print(request.POST.get('username'))
        invite_user=Account.objects.filter(username = request.POST.get('username')).first()
        data={}
        if invite_user:
            event_post.invited_user.add(invite_user)
            event_post.save()
            data["response"]="Success"
        else:
            data["response"]="Failed"
        return Response(data=data)




@api_view(['GET','POST'])
@permission_classes((IsAuthenticated, ))
def api_event_accept_invite_view(request):
    if request.method == "GET":
        queryset = EventPost.objects.filter(invited_user = request.user)
        serializer = EventPostSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        try:
            event_post = EventPost.objects.get(slug=request.POST.get('slug'))
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


        if (request.user in event_post.invited_user.all()) or (event_post.private == False):
            attending_events = EventPost.objects.filter(attending_users = request.user)
            for event in attending_events:
                if is_time_between(event.start_time, event.end_time, event_post.start_time) or is_time_between(event.start_time, event.end_time, event_post.end_time):
                    return Response({"response": "You have already Scheduled Events in this time !"})
            event_post.attending_users.add(request.user)
            event_post.save()
            return Response({"response":"Success"})
        else:
            return Response({"response": "You are not Invited !"})
            



# # Headers: Authorization: Token <token>
class ApiEventListView(ListAPIView):
    queryset = EventPost.objects.filter(private=False)
    serializer_class = EventPostSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title', 'description', 'organizer_username')

