from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm
from users.models import User


class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save()
        self.send_welcome_mail(user.email)
        return super().form_valid(form)

    def send_welcome_mail(self, user_email):
        subject = "Добро пожаловать на наш сайт"
        message = "Спасибо, что зарегистрировались на нашем сайте MoS!"
        from_email = EMAIL_HOST_USER
        recipient_list = [user_email,]
        send_mail(subject, message, from_email, recipient_list)
