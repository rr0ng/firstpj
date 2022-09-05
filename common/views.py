from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator  

def index(request):
    return render(request, 'common/index.html')

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect(index)
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})

def users(request):
    page = request.GET.get('page', '1')  # 페이지
    users_list = get_user_model().objects.all()
    paginator = Paginator(users_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'users_list': page_obj}
    return render(request, 'common/users.html', context)

