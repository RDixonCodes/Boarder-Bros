import email
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from boarder__app.models import*
import bcrypt
# from guest_user.decorators import allow_guest_user


def index(request):

    return render(request,'index.html')

def registration_page(request):

    return render(request,'landing.html')

# @allow_guest_user
def user_register(request):
    if request.method == "POST":

        errors = User.objects.registration_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        
        hash_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()

        new_user = User.objects.create(
            user_name = request.POST['user_name'],
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            user_image = request.POST['user_image'],
            email = request.POST['email'],
            password = hash_pw
        )
        request.session['logged_user'] = new_user.id

        return redirect('/success')
    return redirect('/')

def login(request):
    if request.method == "POST":
        user = User.objects.filter(email = request.POST['email'])

        if user:
            log_user = user[0]

            if bcrypt.checkpw(request.POST['password'].encode(), log_user.password.encode()):
                request.session['logged_user'] = log_user.id
                return redirect('/success')
            messages.error(request, "Email or password are incorrect.")

    return redirect('/')


def success(request):
    logged_user = User.objects.get(id = request.session['logged_user'])
    context = {
        'logged_user': logged_user,
        'all_items': Item.objects.filter(~Q(traded_item = request.session['logged_user'])),
        'logged_user_items': Item.objects.filter()
        }
    return render(request,'dashboard.html', context)

def add(request):
    if request.method == 'POST':
        errors = Item.objects.item_validator(request.POST)

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/add/items')

        user = User.objects.get(id=request.session['logged_user'])
        new_item = Item.objects.create(
            title = request.POST['title'],
            catagory = request.POST['catagory'],
            price = request.POST['price'],
            item_photo_url = request.POST['item_photo_url'],
            desc = request.POST['desc'],
            user_item = user
        )
        user.user_items.add(new_item)
    return redirect(f'/items/list')

def view_items(request):

    context = {
        'logged_user': User.objects.get(id=request.session['logged_user']),
        'all_items': Item.objects.all()
    }

    return render(request, 'product_list.html', context)

def delete_items(request, item_id):
    if 'logged_user' not in request.session:
        messages.error(request, "Please register or log in first")

    item = Item.objects.get(id = item_id)
    item.delete()
    return redirect(f'/items/list')


def logout(request):
    request.session.flush()
    return redirect('/')
# Create your views here.
