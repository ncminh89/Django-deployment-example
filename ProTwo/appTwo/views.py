from django.shortcuts import render
from appTwo.form  import NewUserForm
from appTwo.models import User
# Create your views here.
def index(request):
    return render(request,"appTwo/index.html")

def users(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit = True)
            return index(request)
        else:
            print("Error from invalid")

    return render(request,"appTwo/user.html", {'form':form})

def users_list(request):
    users_list = User.objects.order_by('last_name')
    return render(request,"appTwo/user_list.html",{"users":users_list})
