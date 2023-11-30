from django.utils.decorators import method_decorator
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import CustomUser
from .tasks import send_welcome_email


@method_decorator(csrf_exempt, name='dispatch')
class RegisterUserView(View):
    def post(self, request):
        username = request.POST.get('username')
        if CustomUser.objects.filter(username=username).exists():
            return JsonResponse({'message': 'User with this username already exists'}, status=400)
        email = request.POST.get('email')
        if CustomUser.objects.filter(email=email).exists():
            return JsonResponse({'message': 'User with this email already exists'}, status=400)

        user = CustomUser.objects.create(username=username, email=email)
        send_welcome_email.delay()

        return JsonResponse({'message': 'User created successfully'})
