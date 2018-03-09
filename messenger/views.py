from django.shortcuts import render,get_object_or_404
from .models import Message

# Create your views here.
from django.shortcuts import render

# Create your views here.
def inbox(request):
    return render(request, 'messenger/inbox.html')
    
def sent(request):
    return render(request, 'messenger/sent.html')
    
    
def view_message(request,id):
    item=get_object_or_404(Message,pk=id)
    return render(request, 'messenger/view_message.html',{'item':item})
    
    
def compose(request):
    return render(request, 'messenger/compose.html')
    



