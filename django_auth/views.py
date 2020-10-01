from fcm_django.models import FCMDevice
from django.http import JsonResponse

def notif(request):
    devices = FCMDevice.objects.filter(user__phone_number='08159371542')
    for device in devices:
       device.send_message(title="Title", body="Body", data={"test": "test"})
       break

    return JsonResponse({'status':'OK'})