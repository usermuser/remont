from django.shortcuts import render, get_object_or_404
#http://127.0.0.1:8000/%2Fprices1/
from .models import Device


'''def index(request):
    all_device_list = Device.objects.all()
    context = {'all_device_list': all_device_list }
    return render(request, 'apple_app/index_3.html', context)'''
def index(request):
    all_device_list = Device.objects.all()
    device = get_object_or_404(Device, pk=1)
    context = {'all_device_list': all_device_list, 'device': device }
    return render(request, 'apple_app/index_3.html', context)

'''def detail(request, device_id):
    device = get_object_or_404(Device, pk=device_id)
    return render(request, 'apple_app/detail.html', {'device': device})  '''

'''def detail(request, device_id):
    device = get_object_or_404(Device, pk=device_id)
    return render(request, 'apple_app/detail.html', {'device': device,})'''

def detail(request, device_id):
    all_device_list = Device.objects.all()
    device = get_object_or_404(Device, pk=device_id)
    context = {'all_device_list': all_device_list, 'device': device }
    return render(request, 'apple_app/index_3.html', context)