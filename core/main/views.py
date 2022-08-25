from django.shortcuts import render
from django.views.generic import ListView
from .models import HomeBG, TUser
# Create your views here.
class HomeListView(ListView):
    template_name='home.html'

    def get(self, request):
        bg = HomeBG.objects.all()
        t_user =TUser.objects.all()
        return render(request, self.template_name, {'bg':bg}, {'t_user':t_user})