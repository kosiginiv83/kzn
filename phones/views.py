from rest_framework import viewsets, decorators, serializers, response, status, permissions
# from django.db.models.
import string
import random
import datetime
from django.db.models import ObjectDoesNotExist
from urllib.request import urlopen
from .models import Phone, Code


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ('id', 'phone')


class CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Code
        fields = ('id', 'code')


def randomString(stringLength=5):
    """Generate a random string of fixed length """
    letters = string.digits
    return ''.join(random.choice(letters) for i in range(stringLength))


class PhoneViewSet(viewsets.ViewSet):
    @decorators.action(methods=['post'], detail=False, permission_classes=[permissions.AllowAny])
    def code(self, request):
        serializer = PhoneSerializer(data=request.data)
        if serializer.is_valid():
            phone = Phone.objects.get_or_create(phone=serializer.data['phone'])[0]
            code = Code.objects.create(phone=phone, code=randomString(),
                                       end=datetime.datetime.now() + datetime.timedelta(minutes=20))
            url = 'https://sms.ru/sms/send?api_id=903cf685-12bd-b4e4-31ef-a57dd97efe4b&json=1&to=%s&msg=Your+code+%s' % (
                phone.phone, code.code)
            urlopen(url)
            return response.Response({'status': 'ok'})
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @decorators.action(methods=['post'], detail=False, permission_classes=[permissions.AllowAny])
    def check(self, request):
        serializer = CodeSerializer(data=request.data)
        if serializer.is_valid():
            try:
                code = Code.objects.get(code=serializer.data['code'], phone__phone=request.data['phone'],
                                        end__gt=datetime.datetime.now())
            except ObjectDoesNotExist:
                return response.Response({'errors': 'not exist'})
            code.end = datetime.datetime.now()
            code.save()
            return response.Response({'status': 'ok'})
        return response.Response(serializer.errors)
