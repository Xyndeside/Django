from django.shortcuts import render

from notices.models import Notice


# Create your views here.

def notice_list(request):
    notices = Notice.objects.all().order_by('-created_at')
    return render(request, 'notice_list.html', {'notices': notices})
