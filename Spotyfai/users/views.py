from django.shortcuts import render
from django.http import HttpResponse
from .models import User

#create users

def create_user(request):
    new_user = User.objects.create(name_user = "Angel",
                                   account = "angel@gmail.com",
                                   telephone = "735 233 3245",
                                   premiun = True)
    return HttpResponse("Usuario Creado")

#delete users

def delete_user(request):
    id_user = 1
    rm_user = User.objects.get(id = id_user)
    name_rm_user = rm_user.name_user
    rm_user.delete()
    return HttpResponse(f"user: {name_rm_user} to delete")

#reset for data users

def reset_data_user(request):
    reset_id_data_user = 1
    try:
        data_reset_user = User.objects.get(id = reset_id_data_user)
    except User.DoesNotExist:
        return HttpResponse(f"User of id {reset_id_data_user} not exist")
    data = {
        "name_user":data_reset_user.name,
        "account_user":data_reset_user.account,
        "telephone_user":data_reset_user.telephone,
        "premiun_user":data_reset_user.premiun,
    }
    return render(request, {"list_data_user":data})

#get_all_user

def get_all_user(request):
    all_user = User.objects.all()
    return render(request, {"lis_user" : all_user})

#filter users